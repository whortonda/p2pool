from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['bitcoin']
SHARE_PERIOD = 300 # seconds
CHAIN_LENGTH = 100 # shares
REAL_CHAIN_LENGTH = 100 # shares
TARGET_LOOKBEHIND = 50 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'fc70035c7a81bc6f'.decode('hex')
PREFIX = '2472ef181efcd37b'.decode('hex')
P2P_PORT = 65535
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32//2500000
PERSIST = False
WORKER_PORT = 9332
BOOTSTRAP_ADDRS = ''.split(' ')
ANNOUNCE_CHANNEL = '#p2pool'
VERSION_CHECK = lambda v: None if 100000 <= v else 'Bitcoin version too old. Upgrade to 0.11.2 or newer!' # not a bug. BIP65 support is ensured by SOFTFORKS_REQUIRED
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv'])
MINIMUM_PROTOCOL_VERSION = 3200 # 1700 is currently used by the segwit support PR; we need to refuse to connect to those
