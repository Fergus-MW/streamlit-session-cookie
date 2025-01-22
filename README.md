# Streamlit Session Cookie Example

This repository demonstrates how to implement persistent session management in Streamlit using cookies. It provides a simple example of a login system that maintains user sessions across page refreshes and browser restarts.

## Features

- User authentication with test credentials
- "Remember me" functionality using cookies
- Session persistence across page refreshes
- Secure token generation
- Debug information display
- Mobile-friendly

## Installation

1. Clone this repository:

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run main.py
```

2. Open your browser and navigate to the provided URL (typically `http://localhost:8501`)

3. Use one of the test credentials to log in:
- Username: `admin`, Password: `password123`
- Username: `test_user`, Password: `test123`

4. Check the "Remember me" box to maintain your session

## How It Works

The app uses `extra-streamlit-components` to manage cookies for session persistence. Here's a breakdown of the key components:

1. **Cookie Management**: Uses `stx.CookieManager()` to handle cookie operations
2. **Token Generation**: Creates secure tokens using username and timestamp
3. **Session State**: Utilizes Streamlit's session state for temporary storage
4. **Cookie Persistence**: Implements delays to ensure proper cookie setting

Key code snippets:

```python
# Initialize cookie manager
cookie_manager = stx.CookieManager()

# Set cookies with expiry
cookie_manager.set(
    'auth_token',
    token,
    expires_at=expiry,
    key='set_token'
)

# Get cookies
cookies = cookie_manager.get_all(key='get_cookies')
```

## Important Notes

1. This is a demonstration and should not be used in production without proper security measures
2. The token generation is simplified for demonstration purposes
3. In a production environment, you should:
   - Use a secure database for user management
   - Implement proper password hashing
   - Use more secure token generation and validation
   - Add rate limiting and other security measures

## Dependencies

- streamlit
- extra-streamlit-components
- python-dateutil

## Known Issues

1. Cookie setting requires small delays to ensure proper persistence
2. Session restoration might require a page refresh in some cases

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

Apache 2.0 License - feel free to use this code in your own projects.

## Acknowledgments

- Inspired by the Streamlit community's discussions on session management
- Thanks to the creators of `extra-streamlit-components` for the cookie management functionality

## Author

Fergus McKenzie-Wilson

## Support

If you found this helpful, please star the repository!
