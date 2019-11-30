## Selecionar dados MySQL

```sql
CREATE OR REPLACE
VIEW `ativ`.`vw_notasfiscais` AS
select
    `ativ`.`invoice`.`number` AS `codigonota`,
    `ativ`.`customer`.`name` AS `clientnome`,
    `ativ`.`customer`.`address` AS `clientendereco`,
    `ativ`.`service`.`service_description` AS `notadescricao`,
    `ativ`.`invoice_item`.`quantity` AS `notaquantidade`,
    `ativ`.`invoice_item`.`unit_value` AS `notavalorunit`,
    `ativ`.`resource`.`name` AS `notanomerecurso`,
    `ativ`.`department`.`name_department` AS `notafuncaorecurso`,
    `ativ`.`invoice_item`.`tax_percent` AS `notataxaimpostos`,
    `ativ`.`invoice_item`.`discount_percent` AS `notadesconto`,
    round(`ativ`.`invoice_item`.`subtotal`, 2) AS `notasubtotal`,
    (
    select
        sum(`item`.`subtotal`)
    from
        `ativ`.`invoice_item` `item`
    where
        (`item`.`invoice_id` = `ativ`.`invoice`.`number`)) AS `valortotalnota`
from
    (((((`ativ`.`customer`
join `ativ`.`invoice`)
join `ativ`.`invoice_item`)
join `ativ`.`service`)
join `ativ`.`resource`)
join `ativ`.`department`)
where
    ((`ativ`.`resource`.`department` = `ativ`.`department`.`id_department`)
    and (`ativ`.`invoice_item`.`resource_id` = `ativ`.`resource`.`id_resource`)
    and (`ativ`.`invoice_item`.`service_id` = `ativ`.`service`.`service_id`)
    and (`ativ`.`invoice`.`number` = `ativ`.`invoice_item`.`invoice_id`)
    and (`ativ`.`customer`.`id_customer` = `ativ`.`invoice`.`customer_id`))
```

## Gerar BATCH para enviar ao Cassandra

```sql
select concat("INSERT INTO ativ6.nfiscais (chave, codigonota, clientnome, clientendereco, notadesconto, notadescricao, notafuncaorecurso, notanomerecurso, notaquantidade, notasubtotal, notataxaimpostos, notavalorunit, valortotalnota) VALUES ( uuid(),'",codigonota,"','",clientnome,"','", clientendereco,"','", notadesconto,"','", notadescricao,"','", notafuncaorecurso,"','", notanomerecurso,"','", notaquantidade,"','", notasubtotal,"','", notataxaimpostos,"','", notavalorunit,"','", valortotalnota,"');") AS cassandra from vw_notasfiscais
```

### Amostra resultado do Concat MySql
```bash
BEGIN BATCH
INSERT INTO ativ6.nfiscais (chave, codigonota, clientnome, clientendereco, notadesconto, notadescricao, notafuncaorecurso, notanomerecurso, notaquantidade, notasubtotal, notataxaimpostos, notavalorunit, valortotalnota) VALUES ( uuid(),'1543','Cia. Hering','R. Hermann Hering, 1790 - Bom Retiro, Blumenau - SC, 89010-900, Brazil','0.08','Management of Application Server - Wildfly','Sales','Ralph Johnson','8','475.20','0.4','45','8973.240050777793');
INSERT INTO ativ6.nfiscais (chave, codigonota, clientnome, clientendereco, notadesconto, notadescricao, notafuncaorecurso, notanomerecurso, notaquantidade, notasubtotal, notataxaimpostos, notavalorunit, valortotalnota) VALUES ( uuid(),'1543','Cia. Hering','R. Hermann Hering, 1790 - Bom Retiro, Blumenau - SC, 89010-900, Brazil','0','Licenses for Oracle database Enterprise Edition','Service Desk','Richard Helm','24','1176.00','0.4','35','8973.240050777793');
...
APPLY BATCH;
```

## Create keyspace e tabela
```bash
CREATE KEYSPACE ativ6
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

CREATE TABLE ativ6.nfiscais (
    chave uuid,
    codigonota text,
    clientnome text,
    clientendereco text,
    notadescricao text,
    notaquantidade text,
    notavalorunit text,
    notanomerecurso text,
    notafuncaorecurso text,
    notataxaimpostos text,
    notadesconto text,
    notasubtotal text,
    valortotalnota text,
    PRIMARY KEY ( chave, codigonota )
);

DESC ativ6.nfiscais
```

```bash
CREATE TABLE ativ6.nfiscais (
    uuid text,
    codigonota text,
    clientendereco text,
    clientnome text,
    notadesconto text,
    notadescricao text,
    notafuncaorecurso text,
    notanomerecurso text,
    notaquantidade text,
    notasubtotal text,
    notataxaimpostos text,
    notavalorunit text,
    valortotalnota text,
    PRIMARY KEY (uuid, codigonota)
) WITH CLUSTERING ORDER BY (codigonota ASC)
```

## Enviar dados Cassandra
```bash
BEGIN BATCH
INSERT INTO ativ6.nfiscais (chave, codigonota, clientnome, clientendereco, notadesconto, notadescricao, notafuncaorecurso, notanomerecurso, notaquantidade, notasubtotal, notataxaimpostos, notavalorunit, valortotalnota) VALUES ( uuid(),'1527','Continental Tires','Büttnerstraße 25, 30165 Hannover, Germany','0.08','Development of Android App','Software Development','John Vlissides','40','1452.00','0.29','30','11079.700013548136');
INSERT INTO ativ6.nfiscais (chave, codigonota, clientnome, clientendereco, notadesconto, notadescricao, notafuncaorecurso, notanomerecurso, notaquantidade, notasubtotal, notataxaimpostos, notavalorunit, valortotalnota) VALUES ( uuid(),'1527','Continental Tires','Büttnerstraße 25, 30165 Hannover, Germany','0','Licenses for IBM Lotus Notes users','Accounting','Robert Cecil Martin','31','1463.20','0.18','40','11079.700013548136');
INSERT INTO ativ6.nfiscais (chave, codigonota, clientnome, clientendereco, notadesconto, notadescricao, notafuncaorecurso, notanomerecurso, notaquantidade, notasubtotal, notataxaimpostos, notavalorunit, valortotalnota) VALUES ( uuid(),'1280','RIC TV','Rua Amauri Lange Silvério, 450 - Pilarzinho','0','PHP Developer for Software House','Software Development','Erich Gamma','29','2244.60','0.29','60','10877.849983870983');
...
APPLY BATCH;
```