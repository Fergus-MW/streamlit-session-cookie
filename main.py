import streamlit as st
import extra_streamlit_components as stx
import datetime
import hashlib
import time

# Test user credentials - in production, use proper user management/database
TEST_USERS = {
    "admin": "password123",
    "test_user": "test123"
}

def create_token(username):
    # Create a simple token (in production, use more secure methods)
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    token = hashlib.sha256(f"{username}{timestamp}".encode()).hexdigest()
    return token

# Initialize cookie manager
cookie_manager = stx.CookieManager()

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = None

# Check for existing auth data
cookies = cookie_manager.get_all(key='get_cookies')
auth_token = cookies.get('auth_token')
stored_username = cookies.get('stored_username')

# If we have valid cookies and not logged in, restore the session
if auth_token and stored_username and not st.session_state['logged_in']:
    st.session_state['logged_in'] = True
    st.session_state['username'] = stored_username

def handle_login(username, password, remember):
    if username in TEST_USERS and TEST_USERS[username] == password:
        st.session_state['logged_in'] = True
        st.session_state['username'] = username
        
        if remember:
            token = create_token(username)
            # Set cookies that expire in 30 days
            expiry = datetime.datetime.now() + datetime.timedelta(days=30)
            
            # Set auth token cookie
            cookie_manager.set(
                'auth_token',
                token,
                expires_at=expiry,
                key='set_token'
            )
            
            # Small delay to ensure cookie is set
            time.sleep(0.5)
            
            # Set username cookie
            cookie_manager.set(
                'stored_username',
                username,
                expires_at=expiry,
                key='set_username'
            )
            
            # Another small delay to ensure cookie is set
            time.sleep(0.5)
            
            # Force a rerun to ensure cookies are loaded
            st.rerun()
            
        return True
    return False

def handle_logout():
    # Clear session state
    st.session_state['logged_in'] = False
    st.session_state['username'] = None
    
    # Clear cookies
    cookie_manager.delete('auth_token', key='del_token')
    cookie_manager.delete('stored_username', key='del_username')
    
    # Small delay to ensure cookies are cleared
    time.sleep(0.5)
    st.rerun()

# Main app layout
if not st.session_state['logged_in']:
    st.title("Login")
    
    with st.form("login_form", clear_on_submit=True):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        remember = st.checkbox("Remember me")
        submitted = st.form_submit_button("Login")
        
        if submitted:
            if handle_login(username, password, remember):
                st.rerun()
            else:
                st.error("Invalid username or password")
    
    # Show available test credentials
    st.markdown("---")
    st.markdown("### Test Credentials")
    for test_user, test_pass in TEST_USERS.items():
        st.code(f"Username: {test_user}\nPassword: {test_pass}")
else:
    st.title(f"Welcome back, {st.session_state['username']}!")
    st.button("Logout", on_click=handle_logout)

# Debug information (temporary)
st.markdown("---")
st.markdown("### Debug Info")
st.write("Session State:", st.session_state)
cookies = cookie_manager.get_all(key='debug_cookies')
st.write("All Cookies:", cookies)
st.write("Auth Token:", cookies.get('auth_token'))
st.write("Username Cookie:", cookies.get('stored_username'))