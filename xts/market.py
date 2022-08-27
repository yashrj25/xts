import socketio
from datetime import datetime

class MDSocket_io(socketio.Client):
    """A Socket.IO client.
    This class implements a fully compliant Socket.IO web client with support
    for websocket and long-polling transports.
    :param reconnection: 'True'. if the client should automatically attempt to
                         reconnect to the server after an interruption, or
                         'False' to not reconnect. The default is 'True'.
    :param reconnection_attempts: How many reconnection attempts to issue
                                  before giving up, or 0 for infinity attempts.
                                  The default is 0.
    :param reconnection_delay: How long to wait in seconds before the first
                               reconnection attempt. Each successive attempt
                               doubles this delay.
    :param reconnection_delay_max: The maximum delay between reconnection
                                   attempts.
    :param randomization_factor: Randomization amount for each delay between
                                 reconnection attempts. The default is 0.5,
                                 which means that each delay is randomly
                                 adjusted by +/- 50%.
    :param logger: To enable logging set to 'True' or pass a logger object to
                   use. To disable logging set to 'False'. The default is
                   'False'.
    :param binary: 'True' to support binary payloads, 'False' to treat all
                   payloads as text. On Python 2, if this is set to 'True',
                   'unicode' values are treated as text, and 'str' and
                   'bytes' values are treated as binary.  This option has no
                   effect on Python 3, where text and binary payloads are
                   always automatically discovered.
    :param json: An alternative json module to use for encoding and decoding
                 packets. Custom json modules must have 'dumps' and 'loads'
                 functions that are compatible with the standard library
                 versions.
    """

    def __init__(self, user_details, reconnection=True, reconnection_attempts=0, reconnection_delay=1,
                 reconnection_delay_max=50000, randomization_factor=0.5, logger=False, binary=False, json=None,
                 **kwargs):
        self.sid = socketio.Client(logger=True, engineio_logger=True)
        self.eventlistener = self.sid

        self.sid.on('connect', self._on_connect)
        self.sid.on('message', self._on_message)

        """Similarly implement partial json full and binary json full."""
        self.sid.on('1502-json-full', self._on_message1502_json_full)
        self.sid.on('1502-json-partial', self._on_message1502_json_partial)

        self.sid.on('1504-json-full', self._on_message1504_json_full)
        self.sid.on('1504-json-partial', self._on_message1504_json_partial)

        self.sid.on('1505-json-full', self._on_message1505_json_full)
        self.sid.on('1505-json-partial', self._on_message1505_json_partial)

        self.sid.on('1510-json-full', self._on_message1510_json_full)
        self.sid.on('1510-json-partial', self._on_message1510_json_partial)

        self.sid.on('1501-json-full', self._on_message1501_json_full)
        self.sid.on('1501-json-partial', self._on_message1501_json_partial)

        self.sid.on('1105-json-partial', self._on_message1105_json_partial)

        self.sid.on('disconnect', self._on_disconnect)

        """Get the root url from config file"""
        # currDirMain = os.getcwd()
        # configParser = configparser.ConfigParser()
        # configFilePath = path.xts_config #os.path.join(currDirMain, '..\XTConnect_2\config.ini')
        # configParser.read(configFilePath)

        # self.port = configParser.get(uid, 'root_url')
        self.port = user_details['root_url']
        self.userID = user_details['user_id']
        publishFormat = 'JSON'
        # self.broadcastMode = configParser.get(uid, 'broadcastMode')
        self.broadcastMode = user_details['broadcastMode']
        # self.token = token
        self.token = user_details['market_data_access_token']

        port = f'{self.port}/?token='

        self.connection_url = port + self.token + '&userID=' + self.userID + '&publishFormat=' + publishFormat + '&broadcastMode=' + self.broadcastMode

        self.on_connect = None
        self.on_message = None
        self.on_message1502_json_full = None
        self.on_message1504_json_full = None
        self.on_message1505_json_full = None
        self.on_message1510_json_full = None
        self.on_message1501_json_full = None
        self.on_message1502_json_partial = None
        self.on_message1504_json_partial = None
        self.on_message1505_json_partial = None
        self.on_message1510_json_partial = None
        self.on_message1501_json_partial = None
        self.on_message1105_json_partial = None
        self.on_disconnect = None
        self.on_error = None

    def connect(self, headers={}, transports='websocket', namespaces=None, socketio_path='/apimarketdata/socket.io',
                verify=False):
        """Connect to a Socket.IO server.
        :param verify: Verify SSL
        :param url: The URL of the Socket.IO server. It can include custom
                    query string parameters if required by the server.
        :param headers: A dictionary with custom headers to send with the
                        connection request.
        :param transports: The list of allowed transports. Valid transports
                           are 'polling' and 'websocket'. If not
                           given, the polling transport is connected first,
                           then an upgrade to websocket is attempted.
        :param namespaces: The list of custom namespaces to connect, in
                           addition to the default namespace. If not given,
                           the namespace list is obtained from the registered
                           event handlers.
        :param socketio_path: The endpoint where the Socket.IO server is
                              installed. The default value is appropriate for
                              most cases.

        self.url = self.connection_url
        self.connection_headers = headers
        self.connection_transports = transports
        self.connection_namespaces = namespaces
        self.socketio_path = socketio_path
        
        Connect to the socket.
        """
        url = self.connection_url
        """Connected to the socket."""
        print('Connecting...')
        self.sid.connect(url, headers=headers, transports=transports, namespaces=namespaces, socketio_path=socketio_path)
        # print('Waiting...')
        # self.sid.wait()
        """Disconnected from the socket."""
        # self.sid.disconnect()

    def _on_connect(self):
        """Connect from the socket."""
        self.on_connect()
        # print('Market Data Socket connected successfully!')

    def _on_message(self, data):
        """On receiving message"""
        self.on_message(data)
        # print('I received a message!' + data)

    def _on_message1502_json_full(self, data):
        """On receiving message code 1502 full"""
        self.on_message1502_json_full(data)
        # print('I received a 1502 Market depth message!' + data)

    def _on_message1504_json_full(self, data):
        """On receiving message code 1504 full"""
        """On receiving message code 1504 full"""
        self.on_message1504_json_full(data)
        # print('I received a 1504 Index data message!' + data)

    def _on_message1505_json_full(self, data):
        """On receiving message code 1505 full"""
        self.on_message1505_json_full(data)
        # print('I received a 1505 Candle data message!' + data)

    def _on_message1510_json_full(self, data):
        """On receiving message code 1510 full"""
        self.on_message1510_json_full(data)
        # print('I received a 1510 Open interest message!' + data)

    def _on_message1501_json_full(self, data):
        """On receiving message code 1501 full"""
        self.on_message1501_json_full(data)
        # print('I received a 1501 Level1,Touchline message!' + data)

    def _on_message1502_json_partial(self, data):
        """On receiving message code 1502 partial"""
        self.on_message1502_json_partial(data)
        # print('I received a 1502 partial message!' + data)

    def _on_message1504_json_partial(self, data):
        """On receiving message code 1504 partial"""
        self.on_message1504_json_partial(data)
        # print('I received a 1504 Index data message!' + data)

    def _on_message1505_json_partial(self, data):
        """On receiving message code 1505 partial"""
        self.on_message1505_json_partial(data)
        # print('I received a 1505 Candle data message!' + data)

    def _on_message1510_json_partial(self, data):
        """On receiving message code 1510 partial"""
        self.on_message1510_json_partial(data)
        # print('I received a 1510 Open interest message!' + data)

    def _on_message1501_json_partial(self, data):
        """On receiving message code 1501 partial"""
        self.on_message1501_json_partial(data)
        # now = datetime.now()
        # today = now.strftime("%H:%M:%S")
        # print(today, 'in main 1501 partial Level1,Touchline message!' + data + ' \n')

    def _on_message1105_json_partial(self, data):
        """On receiving message code 1105 partial"""
        self.on_message1105_json_partial(data)
        # now = datetime.now()
        # today = now.strftime("%H:%M:%S")
        # print(today, 'in main 1105 partial, Instrument Property Change Event!' + data + ' \n')

        # print('I received a 1105 Instrument Property Change Event!' + data)

    def _on_disconnect(self):
        """Disconnected from the socket"""
        self.on_disconnect()
        # print('Market Data Socket disconnected!')

    def _on_error(self, data):
        """Error from the socket"""
        self.on_error(data)
        # print('Market Data Error', data)

    def get_emitter(self):
        """For getting the event listener"""
        return self.eventlistener