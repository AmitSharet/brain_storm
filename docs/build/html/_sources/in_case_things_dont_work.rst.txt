Just in case things don't work
*******************************

Hello, so everything is supposed to work just fine after you follow the base instructions.
But just in case things don't work you can try the following:

1. Make sure you have docker installed **properly** on your machine.

2. Run: docker run -d -p 5672:5672 rabbitmq

3. Run: docker run -d -p 27017:27017 mongo

4. Run: python -m brain_storm.server run-server rabbitmq://0.0.0.0:5672

5. Run the parsers you want: python -m brain_storm.parsers run-parser pose rabbitmq://0.0.0.0:5672 (you can run any parsers you like, in this example we ran only pose parser)

6. Run:  python -m brain_storm.saver run-saver mongodb://0.0.0.0:27017 rabbitmq://0.0.0.0:5672

7. Run: python -m brain_storm.api run-server

8. Run: python -m Brain_Storm.client upload-sample <mind file>