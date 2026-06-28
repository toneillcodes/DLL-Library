# Binary Specification: w32topl.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\w32topl.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1c0ba4012aa90ae3379f45c5c2ede15edf959902da6bac91246a00f3bb60d0e8`
* **Total Exported Functions:** 79

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 20 | `ToplGetAlwaysSchedule` | `0x1C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `ToplPScheduleValid` | `0x1C30` | 46 | UnwindData |  |
| 56 | `ToplScheduleCacheCreate` | `0x1C70` | 167 | UnwindData |  |
| 57 | `ToplScheduleCacheDestroy` | `0x1D20` | 180 | UnwindData |  |
| 58 | `ToplScheduleCreate` | `0x1DE0` | 433 | UnwindData |  |
| 59 | `ToplScheduleDuration` | `0x1FA0` | 30 | UnwindData |  |
| 60 | `ToplScheduleExportReadonly` | `0x1FD0` | 44 | UnwindData |  |
| 61 | `ToplScheduleImport` | `0x2010` | 320 | UnwindData |  |
| 62 | `ToplScheduleIsEqual` | `0x2160` | 65 | UnwindData |  |
| 63 | `ToplScheduleMaxUnavailable` | `0x21B0` | 299 | UnwindData |  |
| 64 | `ToplScheduleMerge` | `0x22F0` | 302 | UnwindData |  |
| 65 | `ToplScheduleNumEntries` | `0x2430` | 18 | UnwindData |  |
| 66 | `ToplScheduleValid` | `0x2450` | 34 | UnwindData |  |
| 1 | `ToplAddEdgeSetToGraph` | `0x30E0` | 366 | UnwindData |  |
| 2 | `ToplAddEdgeToGraph` | `0x3260` | 256 | UnwindData |  |
| 3 | `ToplDeleteComponents` | `0x3370` | 154 | UnwindData |  |
| 4 | `ToplDeleteGraphState` | `0x3410` | 269 | UnwindData |  |
| 5 | `ToplDeleteSpanningTreeEdges` | `0x3530` | 174 | UnwindData |  |
| 17 | `ToplEdgeSetVtx` | `0x35F0` | 197 | UnwindData |  |
| 21 | `ToplGetSpanningTreeEdgesForVtx` | `0x36C0` | 2,149 | UnwindData |  |
| 49 | `ToplMakeGraphState` | `0x3F30` | 453 | UnwindData |  |
| 51 | `ToplSTHeapAdd` | `0x43C0` | 68 | UnwindData |  |
| 52 | `ToplSTHeapCostReduced` | `0x4410` | 43 | UnwindData |  |
| 53 | `ToplSTHeapDestroy` | `0x4450` | 45 | UnwindData |  |
| 54 | `ToplSTHeapExtractMin` | `0x4490` | 121 | UnwindData |  |
| 55 | `ToplSTHeapInit` | `0x4510` | 182 | UnwindData |  |
| 32 | `ToplHeapCreate` | `0x47F0` | 76 | UnwindData |  |
| 33 | `ToplHeapDestroy` | `0x4850` | 61 | UnwindData |  |
| 34 | `ToplHeapExtractMin` | `0x48A0` | 90 | UnwindData |  |
| 35 | `ToplHeapInsert` | `0x4900` | 141 | UnwindData |  |
| 36 | `ToplHeapIsElementOf` | `0x49A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `ToplHeapIsEmpty` | `0x49D0` | 1,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `ToplFree` | `0x5080` | 84 | UnwindData |  |
| 67 | `ToplSetAllocator` | `0x51B0` | 263 | UnwindData |  |
| 6 | `ToplEdgeAssociate` | `0x5340` | 179 | UnwindData |  |
| 7 | `ToplEdgeCreate` | `0x5400` | 43 | UnwindData |  |
| 8 | `ToplEdgeDestroy` | `0x5440` | 59 | UnwindData |  |
| 9 | `ToplEdgeDisassociate` | `0x5490` | 177 | UnwindData |  |
| 10 | `ToplEdgeFree` | `0x5550` | 65 | UnwindData |  |
| 11 | `ToplEdgeGetFromVertex` | `0x55A0` | 57 | UnwindData |  |
| 12 | `ToplEdgeGetToVertex` | `0x55E0` | 57 | UnwindData |  |
| 13 | `ToplEdgeGetWeight` | `0x5620` | 56 | UnwindData |  |
| 14 | `ToplEdgeInit` | `0x5660` | 53 | UnwindData |  |
| 15 | `ToplEdgeSetFromVertex` | `0x56A0` | 106 | UnwindData |  |
| 16 | `ToplEdgeSetToVertex` | `0x5710` | 106 | UnwindData |  |
| 18 | `ToplEdgeSetWeight` | `0x5780` | 78 | UnwindData |  |
| 22 | `ToplGraphAddVertex` | `0x57E0` | 110 | UnwindData |  |
| 23 | `ToplGraphCreate` | `0x5860` | 43 | UnwindData |  |
| 24 | `ToplGraphDestroy` | `0x58A0` | 59 | UnwindData |  |
| 25 | `ToplGraphFindEdgesForMST` | `0x58F0` | 476 | UnwindData |  |
| 26 | `ToplGraphFree` | `0x5AE0` | 76 | UnwindData |  |
| 27 | `ToplGraphInit` | `0x5B40` | 77 | UnwindData |  |
| 28 | `ToplGraphMakeRing` | `0x5BA0` | 115 | UnwindData |  |
| 29 | `ToplGraphNumberOfVertices` | `0x5C20` | 56 | UnwindData |  |
| 30 | `ToplGraphRemoveVertex` | `0x5C60` | 112 | UnwindData |  |
| 31 | `ToplGraphSetVertexIter` | `0x5CE0` | 83 | UnwindData |  |
| 38 | `ToplIsToplException` | `0x5D40` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `ToplIterAdvance` | `0x5DA0` | 69 | UnwindData |  |
| 40 | `ToplIterCreate` | `0x5DF0` | 32 | UnwindData |  |
| 41 | `ToplIterFree` | `0x5E20` | 65 | UnwindData |  |
| 42 | `ToplIterGetObject` | `0x5E70` | 70 | UnwindData |  |
| 43 | `ToplListAddElem` | `0x5EC0` | 100 | UnwindData |  |
| 44 | `ToplListCreate` | `0x5F30` | 38 | UnwindData |  |
| 45 | `ToplListFree` | `0x5F60` | 142 | UnwindData |  |
| 46 | `ToplListNumberOfElements` | `0x6000` | 56 | UnwindData |  |
| 47 | `ToplListRemoveElem` | `0x6040` | 111 | UnwindData |  |
| 48 | `ToplListSetIter` | `0x60C0` | 83 | UnwindData |  |
| 68 | `ToplVertexCreate` | `0x6120` | 49 | UnwindData |  |
| 69 | `ToplVertexDestroy` | `0x6160` | 61 | UnwindData |  |
| 70 | `ToplVertexFree` | `0x61B0` | 61 | UnwindData |  |
| 71 | `ToplVertexGetId` | `0x6200` | 56 | UnwindData |  |
| 72 | `ToplVertexGetInEdge` | `0x6240` | 72 | UnwindData |  |
| 73 | `ToplVertexGetOutEdge` | `0x6290` | 108 | UnwindData |  |
| 74 | `ToplVertexGetParent` | `0x6310` | 57 | UnwindData |  |
| 75 | `ToplVertexInit` | `0x6350` | 78 | UnwindData |  |
| 76 | `ToplVertexNumberOfInEdges` | `0x63B0` | 56 | UnwindData |  |
| 77 | `ToplVertexNumberOfOutEdges` | `0x63F0` | 56 | UnwindData |  |
| 78 | `ToplVertexSetId` | `0x6430` | 67 | UnwindData |  |
| 79 | `ToplVertexSetParent` | `0x6480` | 111 | UnwindData |  |
