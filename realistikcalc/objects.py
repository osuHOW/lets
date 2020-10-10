from dataclasses import dataclass

@dataclass
class ResultOsu():
    aim : float
    speed :float
    accuracy : float
    pp : float

@dataclass
class ResultMania():
    strain : float
    accuracy : float
    pp : float

@dataclass
class ResultCatch():
    pp : float # lonely LOL

@dataclass
class ResultTaiko():
    strain : float
    accuracy : float
    pp : float
