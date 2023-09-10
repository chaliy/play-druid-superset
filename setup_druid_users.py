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

READ_FROM_SUPERSET_ROLE = "test_read_from_superset"

def create_user_password(user: str, password: str):

    # https://druid.apache.org/docs/latest/operations/security-overview#enable-authorizers

    coordinator_post(f"/druid-ext/basic-security/authentication/db/{USERS_AUTHENTICATOR}/users/{user}")
    coordinator_post(f"/druid-ext/basic-security/authentication/db/{USERS_AUTHENTICATOR}/users/{user}/credentials", 
        data={"password": "my_password"}
    )

    coordinator_post(f"/druid-ext/basic-security/authorization/db/{USERS_AUTHORIZER}/users/{user}")
    
    coordinator_post(f"/druid-ext/basic-security/authorization/db/{USERS_AUTHORIZER}/roles/{READ_FROM_SUPERSET_ROLE}")
    coordinator_post(f"/druid-ext/basic-security/authorization/db/{USERS_AUTHORIZER}/users/{user}/roles/{READ_FROM_SUPERSET_ROLE}")

    permissions = [
        {
            "resource": {
                "type": "DATASOURCE",
                "name": "wiki(.*)"
            },
            "action": "READ"
        }
    ]

    coordinator_post(f"/druid-ext/basic-security/authorization/db/{USERS_AUTHORIZER}/roles/{READ_FROM_SUPERSET_ROLE}/permissions", data=permissions)


create_user_password("test_user", "my_password")

# %%
