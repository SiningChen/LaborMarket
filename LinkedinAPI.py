import oauth2 as oauth
import urllib

client_id = "86d07i0x26fmbs"
client_secret = "QmwPpCpdgYWWhIVM"
redirect_uri = "https://www.google.com/auth/callback"

consumer = oauth.Consumer(client_id, client_secret)
client = oauth.Client(consumer)

authorization_link = "https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=86d07i0x26fmbs&redirect_uri=https://www.google.com/auth/callback&state=aRandomString"

resp, content = client.request(authorization_link, "GET")
if resp['status'] != '200':
    raise Exception("Invalid response %s." % resp['status'])

content_utf8 = str(content, 'utf-8')  # convert binary to utf-8 string
request_token = dict(urllib.parse.parse_qsl(content_utf8))

print("Go to the following link in your browser:", "\n")
print("https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=86d07i0x26fmbs&redirect_uri=http://localhost:8080/szcodes/auth/linkedin&state=aRandomString")

accepted = 'n'
while accepted.lower() == 'n':
    accepted = input('Have you authorized me? (y/n)')  # prompt for input (y)
oauth_verifier = input('What is the PIN?')  # prompt for pin

access_token_url = 'https://api.linkedin.com/uas/oauth/accessToken'
token = oauth.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
token.set_verifier(oauth_verifier)
client = oauth.Client(consumer, token)
resp, content = client.request(access_token_url, "POST")
content8 = str(content, 'utf-8')
access_token = dict(urllib.parse.parse_qsl(content8))

print("Access Token:", "\n")
print("- oauth_token        = " + access_token['oauth_token'] + '\n')
print("- oauth_token_secret = " + access_token['oauth_token_secret'])
print("You may now access protected resources using the access tokens above.")
