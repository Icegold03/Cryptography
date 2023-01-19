from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh


def parameters():
    """this func returns random g, p parameters for DH key exchange. The parameters is given by the cryptography libary. """
    params = dh.generate_parameters(
        generator=2, key_size=512, backend=default_backend())

    numbers = params.parameter_numbers()
    return numbers.g, numbers.p
