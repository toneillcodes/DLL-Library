# Binary Specification: SqlServerSpatial150.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\SqlServerSpatial150.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5593ce1e2a5da1692580b6276a82ac2dcf983c0b305bd07aaead1ddb6cc10b1d`
* **Total Exported Functions:** 79

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 55 | `GeodeticTessellate` | `0x1450` | 50,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `GeodeticTile` | `0x1450` | 50,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `Identity` | `0x1450` | 50,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `Tessellate` | `0x1450` | 50,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `SetOSYieldCallback` | `0xDB40` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `GetBounds` | `0xDCB0` | 189 | UnwindData |  |
| 32 | `Envelope` | `0xDEC0` | 1,984 | UnwindData |  |
| 24 | `Combine` | `0xE690` | 2,425 | UnwindData |  |
| 29 | `CurveToLineWithTolerance` | `0xF010` | 866 | UnwindData |  |
| 22 | `Buffer` | `0xF380` | 2,165 | UnwindData |  |
| 75 | `SimpleBuffer` | `0xFC00` | 1,788 | UnwindData |  |
| 27 | `ConvexHull` | `0x10310` | 2,519 | UnwindData |  |
| 33 | `Equals` | `0x11560` | 1,011 | UnwindData |  |
| 60 | `Intersects` | `0x12510` | 149 | UnwindData |  |
| 61 | `IntersectsV2` | `0x125B0` | 2,357 | UnwindData |  |
| 78 | `Touches` | `0x12EF0` | 125 | UnwindData |  |
| 28 | `Crosses` | `0x12F80` | 140 | UnwindData |  |
| 25 | `Contains` | `0x13020` | 149 | UnwindData |  |
| 26 | `ContainsV2` | `0x130C0` | 2,621 | UnwindData |  |
| 68 | `Overlaps` | `0x13B10` | 123 | UnwindData |  |
| 71 | `Relate` | `0x13BA0` | 130 | UnwindData |  |
| 65 | `Length` | `0x13C30` | 156 | UnwindData |  |
| 20 | `Area` | `0x13CE0` | 832 | UnwindData |  |
| 23 | `Centroid` | `0x14030` | 773 | UnwindData |  |
| 70 | `PointOnSurface` | `0x14340` | 444 | UnwindData |  |
| 62 | `IsSimple` | `0x14510` | 535 | UnwindData |  |
| 30 | `Distance` | `0x14BD0` | 152 | UnwindData |  |
| 31 | `DistanceV2` | `0x14C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `ShortestLine` | `0x14C80` | 521 | UnwindData |  |
| 67 | `Outline` | `0x14E90` | 1,269 | UnwindData |  |
| 58 | `GetGridCoverage` | `0x15390` | 698 | UnwindData |  |
| 63 | `IsValid` | `0x158B0` | 48 | UnwindData |  |
| 64 | `IsValidDetailed` | `0x158F0` | 168 | UnwindData |  |
| 66 | `MakeValid` | `0x159A0` | 47 | UnwindData |  |
| 21 | `Boundary` | `0x159E0` | 1,039 | UnwindData |  |
| 69 | `PlanarReduce` | `0x15E00` | 388 | UnwindData |  |
| 76 | `SingleSideReduce` | `0x15F90` | 1,980 | UnwindData |  |
| 50 | `GeodeticMakeValid` | `0x168A0` | 307 | UnwindData |  |
| 35 | `GeodeticArea` | `0x16CE0` | 1,498 | UnwindData |  |
| 49 | `GeodeticLength` | `0x172C0` | 265 | UnwindData |  |
| 52 | `GeodeticPointDistance` | `0x17D30` | 322 | UnwindData |  |
| 43 | `GeodeticDistance` | `0x18070` | 62 | UnwindData |  |
| 54 | `GeodeticShortestLine` | `0x180C0` | 331 | UnwindData |  |
| 47 | `GeodeticIsValid` | `0x185C0` | 335 | UnwindData |  |
| 48 | `GeodeticIsValidDetailed` | `0x18720` | 483 | UnwindData |  |
| 39 | `GeodeticCombine` | `0x18E80` | 1,826 | UnwindData |  |
| 44 | `GeodeticEquals` | `0x19A10` | 1,739 | UnwindData |  |
| 46 | `GeodeticIntersects` | `0x1A0F0` | 1,680 | UnwindData |  |
| 40 | `GeodeticContains` | `0x1A790` | 1,034 | UnwindData |  |
| 51 | `GeodeticOverlaps` | `0x1ABA0` | 107 | UnwindData |  |
| 42 | `GeodeticCurveToLineWithTolerance` | `0x1AC20` | 1,498 | UnwindData |  |
| 36 | `GeodeticBuffer` | `0x1B510` | 3,896 | UnwindData |  |
| 45 | `GeodeticGridCoverage` | `0x1C450` | 825 | UnwindData |  |
| 53 | `GeodeticReduce` | `0x1C790` | 842 | UnwindData |  |
| 34 | `GeodeticAngleExtent` | `0x1CAE0` | 336 | UnwindData |  |
| 37 | `GeodeticCapCenter` | `0x1CC40` | 286 | UnwindData |  |
| 79 | `UpdateGeodeticEnvelope` | `0x1CD70` | 440 | UnwindData |  |
| 38 | `GeodeticCapUnion` | `0x1CF30` | 376 | UnwindData |  |
| 41 | `GeodeticConvexHull` | `0x1D0B0` | 1,753 | UnwindData |  |
| 72 | `SetClrFeatureSwitchMap` | `0x1D790` | 21,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `?ComputeBounds@@YAJUGeoData@@PEAV?$CMglRect@N@@@Z` | `0x22CC0` | 382 | UnwindData |  |
| 1 | `??0GeoBundle@@QEAA@PEBUGeoData@@@Z` | `0x29F10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0GeoBundle@@QEAA@PEBUGeoData@@_N1@Z` | `0x29F60` | 192 | UnwindData |  |
| 6 | `?FCascadeEliminationEnabled@GeoBundle@@QEBA_NXZ` | `0x2A120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `?IncResidualCost@GeoBundle@@QEAAX_K@Z` | `0x2A130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `?GetNextCascadeAreaReduceFactor@GeoBundle@@QEBANXZ` | `0x2A150` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `?UpdateNextCascadeCost@GeoBundle@@QEAAXXZ` | `0x2A1E0` | 32 | UnwindData |  |
| 7 | `?GetCascadesSaving@GeoBundle@@QEBA_JXZ` | `0x2A4D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `?StopAddingNewCascades@GeoBundle@@QEAAXXZ` | `0x2A500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `?FAddNewCascade@GeoBundle@@QEBA_NAEAH@Z` | `0x2A510` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0SpatialIntrisicCostInfo@GeoBundle@@QEAA@XZ` | `0x2A580` | 317,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `?m_Weights1@SampleDescriptor@@2QBNB` | `0x77C00` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `?m_Weights3@SampleDescriptor@@2QBNB` | `0x77C08` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `?m_Weights2@SampleDescriptor@@2QBNB` | `0x77C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `?m_Weights6@SampleDescriptor@@2QBNB` | `0x77C30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `?m_Points6@SampleDescriptor@@2QBNB` | `0x77C60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `?m_Points3@SampleDescriptor@@2QBNB` | `0x77C90` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `?m_Points2@SampleDescriptor@@2QBNB` | `0x77CA8` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `?m_Points1@SampleDescriptor@@2QBNB` | `0x77CB8` | 0 | Indeterminate |  |
