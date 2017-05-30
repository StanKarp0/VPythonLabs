from __future__ import division
import e01

with open("file.txt", "w") as file_data:
    res = [(e01.probability(dim), e01.v(dim)) for dim in range(2, 10)]
    toSave = [", ".join([str(r), str(p), str(p/r)]) for p, r in res]
    r = "\n".join(toSave)
    print r
    file_data.write(r)
