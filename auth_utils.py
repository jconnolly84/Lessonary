import os

def get_google_login_url():
    client_id = os.environ.get("google_oauth_client_id")
    redirect_uri = os.environ.get("google_oauth_redirect_uri")
    scope = "openid email profile"
    return (
        f"https://accounts.google.com/o/oauth2/auth"
        f"?response_type=code&client_id={client_id}"
        f"&redirect_uri={redirect_uri}"
        f"&scope={scope}&access_type=offline&prompt=consent"
    )

def get_ms_login_url():
    client_id = os.environ.get("ms_client_id")
    tenant_id = os.environ.get("ms_tenant_id")
    redirect_uri = os.environ.get("ms_redirect_uri")
    scope = "openid email profile offline_access"
    return (
        f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/authorize"
        f"?client_id={client_id}"
        f"&response_type=code"
        f"&redirect_uri={redirect_uri}"
        f"&response_mode=query"
        f"&scope={scope}&prompt=select_account"
    )