# Hashgen

A simple Python script for generating a variety of hashes from safe urandom entropy.

For whenever you need a random hash (e.g. setting an app secret) or a random password (although [random words make for better passwords](https://xkcd.com/936/)).

## Disclaimer

This is a personal hobby project. It has not been audited. However it is using urandom for entropy and makes use of industry standard hashing algorithms, I have not "rolled my own crypto." If you are particularly concerned with security I recommend using at least 384 bit hashes.
