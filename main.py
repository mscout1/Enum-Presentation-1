from enum import Enum, auto


class CourtType(Enum):
    SCOTUS = auto()
    FEDERAL_CIRCUIT = auto()
    FEDERAL_DISTRICT = auto()
    STATE_SUPREME = auto()
    STATE_APPLETTE = auto()
    STATE_TRIAL = auto()


print("Iterate and Print")
for court in CourtType:
    print(court)

print("\n\nEnum Types are Containers")
print(f"{len(CourtType)=}")
print(f"{CourtType.SCOTUS in CourtType=}")
try:
  print(f"{2 in CourtType=}")
except Exception as e:
    print(f"2 in CourtType->{e}")

print("\n\nEnums have values and names")
for court in CourtType:
    print(f"{court.value=}; {court.name=}")

print("\nValue Lookups")
print(f"{CourtType(1)=}")

print("\nName Lookups")
print(f"{CourtType.STATE_TRIAL=}")
print(f"{getattr(CourtType, 'STATE_TRIAL')=}")

try:
    print(f"{CourtType('STATE_TRIAL')=}")
except Exception as e:
    print(f"CourtType('STATE_TRIAL')->{e}")

print("\nSelf Lookups")
print(f"{CourtType(CourtType.STATE_APPLETTE)=}")
