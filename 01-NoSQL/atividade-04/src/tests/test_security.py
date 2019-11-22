import werkzeug 

def test_CVE_2019_14806():
    """
    CVE-2019-14806
    high severity
    Vulnerable versions: < 0.15.3
    Patched version: 0.15.3
    https://github.com/advisories/GHSA-gq9m-qvpx-68hc

    Pallets Werkzeug before 0.15.3, when used with Docker, 
    has insufficient debugger PIN randomness because 
    Docker containers share the same machine id.
    """
    werkzeug_version = tuple(map(int, werkzeug.__version__.split('.')))
    secure_version = (0, 15, 3)
    
    assert werkzeug_version >= secure_version
