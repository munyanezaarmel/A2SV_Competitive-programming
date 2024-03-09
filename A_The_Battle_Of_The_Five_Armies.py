
damage_capabilities = list(map(int, input().split()))
army_sizes = list(map(int, input().split()))
bilbos_power = sum(capability * size for capability, size in zip(damage_capabilities[:3], army_sizes[:3]))

opposing_power = sum(capability * size for capability, size in zip(damage_capabilities[3:], army_sizes[3:]))

if bilbos_power > opposing_power:
    print("WIN")
elif bilbos_power < opposing_power:
    print("LOSE")
else:
    print("DRAW")
