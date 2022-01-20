# Hashgen

A simple Python script for generating a variety of hashes from safe urandom entropy.

For whenever you need a random hash (e.g. generating an app secret) or a random password (although [random words make for better passwords](https://xkcd.com/936/)).

## How to use

Download the script, either `cd` to it or put it somewhere in your path, then simply run the script followed by the hashing algorithm of your choice. Running the script with no arguments will present this help page:

```
usage: hashgen [-h] [--blake2b] [--sha3] [--sha256] [--sha384] [--sha512] [--version]

Generate a random blake2b, SHA3-384, SHA256, SHA384, or SHA512 hash using safe entropy from urandom.

optional arguments:
  -h, --help      show this help message and exit
  --blake2b, -b   hashes random entropy using blake2b
  --sha3, -3      hashes random entropy using sha3-384
  --sha256, -256  hashes random entropy using sha256
  --sha384, -384  hashes random entropy using sha384
  --sha512, -512  hashes random entropy using sha512
  --version, -v   show program version and exit

https://github.com/X448NAX/Hashgen
```

Usage example, assuming the script is in your path:

```
hashgen --blake2b
4de2ca0a16e9f8a038e0d53639a00c8b010d6e164a868a149a40a875438f1c92f232b2bf1cda1d9d06d36407a2359ed2f9ba766330d529c8978a6a575a695f1e
```

If it's not in your path:

```
python3 hashgen.py -3
26b75e69d89497c00b12430de11f1693da47ce537f9a4f2aad8e145a977f92c7ae8c617ecfa26109524d914dcba9af68
```

Simple as that!

## Future functionality

I plan to add functionality to this here and there. If there's something you think would benefit it feel free to submit a PR.

## Dependencies

None. Hashgen was created specifically to only use hash functions built into the native Python hashlib library. If you are having issues, make sure you are using at least Python 3.6. I tested against 3.9 when creating this.

Additional hashes from third party libraries may be added in the future, but core functionality will be focused on those natively supported by Python.

## Disclaimer

This is a personal hobby project. It has not been audited. However it is using urandom for entropy and makes use of industry standard hashing algorithms, I have not "rolled my own crypto." If you are particularly concerned with security I recommend using at least 384 bit hashes.

Algorithms with known practical hash collision attacks such as MD5 and SHA1 are not and will not be included.
