from abc import ABC, abstractmethod, abstractproperty

class Material(ABC):
    young_modulus = 0
    poisson_ratio = 0
    density = 0
    