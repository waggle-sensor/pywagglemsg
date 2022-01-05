import unittest
import wagglemsg


class TestMain(unittest.TestCase):

    def test_fail(self):
        test_cases = [
            wagglemsg.Message(
                name='env.temperature.htu21d',
                value=10,
                timestamp=1602704769215113000,
                meta={},
            ),
            wagglemsg.Message(
                name='env.temperature.htu21d',
                value=21.2,
                timestamp=1602704769215113000,
                meta={},
            ),
            wagglemsg.Message(
                name='env.temperature.htu21d',
                value=b'some binary data',
                timestamp=1602704769215113000,
                meta={},
            ),
            wagglemsg.Message(
                name='env.temperature.htu21d',
                value='some string data',
                timestamp=1602704769215113000,
                meta={
                    "id": "meta-test-id"
                },
            )
        ]

        for msg in test_cases:
            out = wagglemsg.load(wagglemsg.dump(msg))
            self.assertEqual(msg, out)



if __name__ == "__main__":
    unittest.main()
