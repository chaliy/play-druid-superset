# %%
import requests

BASE_COORDINATOR_URL = "http://localhost:8081"

def coordinator_post(path: str, data: dict = None):
    resp = requests.post(f"{BASE_COORDINATOR_URL}{path}", 
        json=data,
        auth=("admin", "password1")
    )
    print(f'{resp.status_code} : {resp.reason} \n {resp.text}')

USERS_AUTHENTICATOR = "Users"
USERS_AUTHORIZER = "UsersAuthorizer"

def create_user_password(user: str, password: str, role: str, permissions: list):

    # https://druid.apache.org/docs/latest/operations/security-overview#enable-authorizers

    coordinator_post(f"/druid-ext/basic-security/authentication/db/{USERS_AUTHENTICATOR}/users/{user}")
    coordinator_post(f"/druid-ext/basic-security/authentication/db/{USERS_AUTHENTICATOR}/users/{user}/credentials", 
        data={"password": "my_password"}
    )

    coordinator_post(f"/druid-ext/basic-security/authorization/db/{USERS_AUTHORIZER}/users/{user}")
    
    coordinator_post(f"/druid-ext/basic-security/authorization/db/{USERS_AUTHORIZER}/roles/{role}")
    coordinator_post(f"/druid-ext/basic-security/authorization/db/{USERS_AUTHORIZER}/users/{user}/roles/{role}")
    coordinator_post(f"/druid-ext/basic-security/authorization/db/{USERS_AUTHORIZER}/roles/{role}/permissions", data=permissions)


create_user_password("wiki-reader-1", "secretpassword", "wiki-reader",  [
    {
        "resource": {
            "type": "DATASOURCE",
            "name": "wiki(.*)"
        },
        "action": "READ"
    }
])

# %%
