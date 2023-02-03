import dill as pickle


class SerializationUtils:
    """
        Utility class for serialization and deserialization
    """
    @staticmethod
    def serialize(obj, path):
        file = open(path, "wb")
        #
        pickle.dump(obj, file)
        #
        file.close()

    @staticmethod
    def deserialize(path):
        file = open(path, "rb")
        #
        ret = pickle.load(file)
        #
        file.close()
        #
        return ret
