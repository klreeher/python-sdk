#Import the OrderCloud SDK
import OrderCloud as oc
import pytest
from .rest import ApiException


def test_auth_noise():
    """
        things that should fail
    """

    assert oc.configuration.client_id is None
    assert oc.configuration.access_token is None
    assert oc.configuration.username is None
    assert oc.configuration.password is None

    with pytest.raises(ApiException) as excinfo:
        oc.auth.authenticate()
    print(str(excinfo.value))
    





def test_auth_signal()
    """
        things that should not fail
    """

    oc.configuration.client_id = "1AA9B54E-B31D-48E6-94E2-7454208D82E0" #Grab your Client ID from the OrderCloud Developer Center and paste it here! 
    oc.configuration.scopes = ["Shopper"]

    # auth as anon shopper

    oc.auth.authenticate()
    user = oc.MeApi.get()

    oc.configuration.access_token = ''

    # profile anon shopper



    #log in with username and password
    oc.auth.login("testuser01","fails345!!")
    #This will acquire an access token and store it in oc.configuration.access_token

    #Now we can use the API, to check if everything worked, this should return the currently authenticated user.
    user = oc.MeApi.get()

