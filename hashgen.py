from hashlib import blake2b, sha512, sha256, sha384, sha3_384, sha3_512, shake_256
import secrets
import argparse
import sys

parser = argparse.ArgumentParser(prog='hashgen',epilog='https://github.com/X448NAX/Hashgen',description='Generate a random blake2b, SHA3-384, SHA3-512, SHAKE256, SHA256, SHA384, or SHA512 hash using safe entropy from urandom.')
parser.version = 'hashgen v1.0.2'
parser.add_argument("--blake2b", "-b", help="hashes random entropy using blake2b", dest="blake2b", action="store_true")
parser.add_argument("--sha3", "-3", help="hashes random entropy using sha3-384", dest="sha3", action="store_true")
parser.add_argument("--sha3512", "-35", help="hashes random entropy using sha3-512", dest="sha3512", action="store_true")
parser.add_argument("--shake256", "-shake", help="hashes random entropy using shake-256", dest="shake256", action="store_true")
parser.add_argument("--sha256", "-256", help="hashes random entropy using sha256", dest="sha256", action="store_true")
parser.add_argument("--sha384", "-384", help="hashes random entropy using sha384", dest="sha384", action="store_true")
parser.add_argument("--sha512", "-512", help="hashes random entropy using sha512", dest="sha512", action="store_true")
parser.add_argument("--version", "-v", help="show program version and exit", action='version')
if len(sys.argv) < 2:
	parser.print_help()
	sys.exit(1)
parser.parse_args()

entropy = secrets.token_bytes(64)
blake2b = blake2b(entropy).hexdigest()
sha256hash = sha256(entropy).hexdigest()
sha384hash = sha384(entropy).hexdigest()
sha512hash = sha512(entropy).hexdigest()
sha3_384hash = sha3_384(entropy).hexdigest()
sha3_512hash = sha3_512(entropy).hexdigest()
shake256hash = shake_256(entropy).hexdigest(length=42)

args = parser.parse_args()

if args.blake2b:
	print(blake2b)
if args.sha256:
	print(sha256hash)
if args.sha384:
	print(sha384hash)
if args.sha512:
	print(sha512hash)
if args.sha3:
	print(sha3_384hash)
if args.sha3512:
	print(sha3_512hash)
if args.shake256:
	print(shake256hash)
