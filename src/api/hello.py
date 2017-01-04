from src import service


def get_auth_profile(input_headers):
  if 'Authorization' not in input_headers:
    return None
  value = input_headers['Authorization']
  if not value.startswith("Bearer "):
    raise Exception("'Authorization' header is malformatted - does not start with 'Bearer '")
  token = value[7:]
  return jwt.decode(token, 'SECRET_THAT_ONLY_THIS_SERVICE_KNOWS_ABOUT')





@service.api("/hello")
def hello(input_headers, input_data):
  """
  Construct and return a greeting string
  """

  auth_profile = get_auth_profile(input_headers)
  if not auth_profile:
    raise Exception("Not authorized")

  return "Hello " + auth_profile['first_name']






import jwt

@service.api(
  "/get-jwt",
  input_format={
    "[email_address_password]": {
      "email_address": str,
      "password": str
    },
    "[facebook_token]": str
  }
)
def get_jwt(input_headers, input_data):
  # You could do simple username / password authentication that you manage directly
  # Or you could take in a "socialToken" like form FB and call off to FB to verify that authenticity of that token
  # https://ole.michelsen.dk/blog/social-signin-spa-jwt-server.html

  # Here's a library for generating / decoding JWTs:
  # https://github.com/jpadilla/pyjwt


  # TEST
  import uwsgi
  from datetime import datetime
  uwsgi.set_logvar('iso_datetime', datetime.utcnow().isoformat() + "Z")


  if "email_address_password" in input_data:
    print input_data
    email_address = input_data["email_address_password"]["email_address"]
    password = input_data["email_address_password"]["password"]
    if email_address.lower() == "alexexarhos@gmail.com" and password == "123":
      return jwt.encode({
        "first_name": "Alex",
        "email_address": "alexexarhos@gmail.com"
      }, 'SECRET_THAT_ONLY_THIS_SERVICE_KNOWS_ABOUT')

  if "facebook_token" in input_data:
    # Call off to FB to get the user information associated with this token...
    return jwt.encode({
        "first_name": "Alex",
        "email_address": "alexexarhos@gmail.com"
      }, 'SECRET_THAT_ONLY_THIS_SERVICE_KNOWS_ABOUT')

  raise Exception("Not authorized")


"""
If you want to communicate with a service, then you need to fetch a corresponding JWT that grants you permission to do so.


https://auth0.com/docs/jwt

{
  "issuer":

What are the various ways to manage authentication?
- email / password



"""
