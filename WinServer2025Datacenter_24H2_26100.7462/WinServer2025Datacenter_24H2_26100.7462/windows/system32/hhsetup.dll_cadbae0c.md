# Binary Specification: hhsetup.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\hhsetup.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cadbae0cb8c825fbf1124716cb983f51ca729a3ef814f3a5a7959c691e800efe`
* **Total Exported Functions:** 145

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `??0CCollection@@QEAA@XZ` | `0x1A40` | 223 | UnwindData |  |
| 2 | `??0CFIFOString@@QEAA@XZ` | `0x1B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0CPointerList@@QEAA@XZ` | `0x1B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0CFolder@@QEAA@XZ` | `0x1B40` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0CLocation@@QEAA@XZ` | `0x1B90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0CTitle@@QEAA@XZ` | `0x1BC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??1CCollection@@QEAA@XZ` | `0x1BF0` | 52 | UnwindData |  |
| 9 | `??1CFolder@@QEAA@XZ` | `0x1C30` | 43 | UnwindData |  |
| 10 | `??1CLocation@@QEAA@XZ` | `0x1C70` | 127 | UnwindData |  |
| 11 | `??1CPointerList@@QEAA@XZ` | `0x1D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??1CTitle@@QEAA@XZ` | `0x1D10` | 164 | UnwindData |  |
| 13 | `??4CCollection@@QEAAAEAV0@AEBV0@@Z` | `0x1DC0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??4CFIFOString@@QEAAAEAV0@AEBV0@@Z` | `0x1E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??4CPointerList@@QEAAAEAV0@AEBV0@@Z` | `0x1E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??4CFolder@@QEAAAEAV0@AEBV0@@Z` | `0x1E80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `??4CLocation@@QEAAAEAV0@AEBV0@@Z` | `0x1EC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??4CTitle@@QEAAAEAV0@AEBV0@@Z` | `0x1F00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `?Add@CPointerList@@QEAAPEAUListItem@@PEAX@Z` | `0x1F30` | 56 | UnwindData |  |
| 20 | `?AddChildFolder@CFolder@@QEAAKPEAV1@@Z` | `0x1F70` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `?AddChildFolder@CFolder@@QEAAPEAV1@PEBDKPEAKG@Z` | `0x2000` | 181 | UnwindData |  |
| 22 | `?AddChildFolder@CFolder@@QEAAPEAV1@PEBGKPEAKG@Z` | `0x20C0` | 102 | UnwindData |  |
| 23 | `?AddCollection@CCollection@@QEAAPEAVCColList@@XZ` | `0x2130` | 85 | UnwindData |  |
| 24 | `?AddFolder@CCollection@@QEAAPEAVCFolder@@PEBDKPEAKG@Z` | `0x2190` | 306 | UnwindData |  |
| 25 | `?AddFolder@CCollection@@QEAAPEAVCFolder@@PEBGKPEAKG@Z` | `0x22D0` | 102 | UnwindData |  |
| 26 | `?AddLocation@CCollection@@QEAAPEAVCLocation@@PEBD000PEAK@Z` | `0x2340` | 227 | UnwindData |  |
| 27 | `?AddLocation@CCollection@@QEAAPEAVCLocation@@PEBG000PEAK@Z` | `0x2430` | 221 | UnwindData |  |
| 28 | `?AddLocationHistory@CTitle@@QEAAKKPEBD00PEBVCLocation@@00H@Z` | `0x2520` | 806 | UnwindData |  |
| 29 | `?AddLocationHistory@CTitle@@QEAAKKPEBG00PEBVCLocation@@00H@Z` | `0x2850` | 301 | UnwindData |  |
| 30 | `?AddRef@CCollection@@QEAAXXZ` | `0x2990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `?AddRefedTitle@CCollection@@AEAAKPEAVCFolder@@@Z` | `0x29A0` | 30 | UnwindData |  |
| 33 | `?AddTitle@CCollection@@QEAAPEAVCTitle@@PEBD0000GIPEAVCLocation@@PEAKH0@Z` | `0x29D0` | 356 | UnwindData |  |
| 34 | `?AddTitle@CCollection@@QEAAPEAVCTitle@@PEBG0000GIPEAVCLocation@@PEAKH0@Z` | `0x2B40` | 331 | UnwindData |  |
| 35 | `?AllocCopyValue@CCollection@@AEAAKPEAVCParseXML@@PEADPEAPEAD@Z` | `0x2CA0` | 215 | UnwindData |  |
| 36 | `?AllocSetValue@@YAKPEBDPEAPEAD@Z` | `0x2D80` | 172 | UnwindData |  |
| 37 | `?CheckTitleRef@CCollection@@AEAAKPEBDG@Z` | `0x2E40` | 81 | UnwindData |  |
| 38 | `?CheckTitleRef@CCollection@@AEAAKPEBGG@Z` | `0x2EA0` | 76 | UnwindData |  |
| 39 | `?Close@CCollection@@QEAAKXZ` | `0x2F00` | 411 | UnwindData |  |
| 40 | `?ConfirmTitles@CCollection@@QEAAXXZ` | `0x30B0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `?DecrementRefTitleCount@CCollection@@QEAAXXZ` | `0x3180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `?DeleteChildren@CCollection@@AEAAXPEAPEAVCFolder@@@Z` | `0x3190` | 159 | UnwindData |  |
| 43 | `?DeleteFolder@CCollection@@QEAAKPEAVCFolder@@@Z` | `0x3240` | 121 | UnwindData |  |
| 44 | `?DeleteFolders@CCollection@@AEAAXPEAPEAVCFolder@@@Z` | `0x32C0` | 194 | UnwindData |  |
| 45 | `?DeleteLocalFiles@CCollection@@AEAAXPEAULocationHistory@@PEAVCTitle@@@Z` | `0x3390` | 428 | UnwindData |  |
| 46 | `?DeleteLocation@CCollection@@AEAAKPEAVCLocation@@@Z` | `0x3550` | 138 | UnwindData |  |
| 47 | `?DeleteTitle@CCollection@@AEAAKPEAVCTitle@@@Z` | `0x35E0` | 338 | UnwindData |  |
| 48 | `?Dirty@CCollection@@QEAAXXZ` | `0x3740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `?FindCollection@CCollection@@QEAAPEAVCColList@@PEBD@Z` | `0x3760` | 73 | UnwindData |  |
| 50 | `?FindLocation@CCollection@@QEAAPEAVCLocation@@PEBDPEAI@Z` | `0x37B0` | 131 | UnwindData |  |
| 51 | `?FindLocation@CCollection@@QEAAPEAVCLocation@@PEBGPEAI@Z` | `0x3840` | 76 | UnwindData |  |
| 52 | `?FindTitle@CCollection@@QEAAPEAVCTitle@@PEBDG@Z` | `0x38A0` | 167 | UnwindData |  |
| 53 | `?FindTitle@CCollection@@QEAAPEAVCTitle@@PEBGG@Z` | `0x3950` | 78 | UnwindData |  |
| 54 | `?First@CPointerList@@QEAAPEAUListItem@@XZ` | `0x39B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `?GetId@CLocation@@QEBAPEADXZ` | `0x39B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `?GetId@CTitle@@QEAAPEADXZ` | `0x39B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `?GetTitle@CFolder@@QEAAPEADXZ` | `0x39B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `?FirstLocation@CCollection@@QEAAPEAVCLocation@@XZ` | `0x39C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `?GetColNo@CCollection@@QEAAKXZ` | `0x39D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `?GetCollectionFileName@CCollection@@QEAAPEBDXZ` | `0x39E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `?GetTitle@CLocation@@QEAAPEADXZ` | `0x39E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `?GetCollectionFileNameW@CCollection@@QEAAPEBGXZ` | `0x39F0` | 43 | UnwindData |  |
| 59 | `?GetFindMergedCHMS@CCollection@@QEAAHXZ` | `0x3A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `?GetFirstChildFolder@CFolder@@QEAAPEAV1@XZ` | `0x3A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `?GetFirstTitle@CCollection@@QEAAPEAVCTitle@@XZ` | `0x3A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `?GetNextLocation@CLocation@@QEAAPEAV1@XZ` | `0x3A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `?GetIdW@CLocation@@QEAAPEBGXZ` | `0x3A60` | 42 | UnwindData |  |
| 65 | `?GetIdW@CTitle@@QEAAPEBGXZ` | `0x3A90` | 42 | UnwindData |  |
| 87 | `?GetTitleW@CFolder@@QEAAPEBGXZ` | `0x3A90` | 42 | UnwindData |  |
| 66 | `?GetLangId@CCollection@@QEAAGPEBD@Z` | `0x3AC0` | 207 | UnwindData |  |
| 67 | `?GetLangId@CCollection@@QEAAGPEBG@Z` | `0x3BA0` | 63 | UnwindData |  |
| 68 | `?GetLanguage@CFolder@@QEAAGXZ` | `0x3BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `?GetLanguage@CTitle@@QEAAGXZ` | `0x3C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `?GetLocation@CTitle@@QEAAPEAULocationHistory@@K@Z` | `0x3C10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `?GetMasterCHM@CCollection@@QEAAHPEAPEADPEAG@Z` | `0x3C30` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `?GetMasterCHM@CCollection@@QEAAHPEAPEAGPEAG@Z` | `0x3C70` | 115 | UnwindData |  |
| 73 | `?GetNextFolder@CFolder@@QEAAPEAV1@XZ` | `0x3CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `?GetSampleLocation@CCollection@@QEAAPEADXZ` | `0x3CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `?GetNextTitle@CTitle@@QEAAPEAV1@XZ` | `0x3D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `?GetVolume@CLocation@@QEAAPEADXZ` | `0x3D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `?GetOrder@CFolder@@QEAAKXZ` | `0x3D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `?GetParent@CFolder@@QEAAPEAV1@XZ` | `0x3D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `?GetPath@CLocation@@QEAAPEADXZ` | `0x3D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `?GetPathW@CLocation@@QEAAPEBGXZ` | `0x3D40` | 43 | UnwindData |  |
| 80 | `?GetRefTitleCount@CCollection@@QEAAKXZ` | `0x3D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `?GetRootFolder@CCollection@@QEAAPEAVCFolder@@XZ` | `0x3D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `?GetSampleLocationW@CCollection@@QEAAPEBGXZ` | `0x3DA0` | 43 | UnwindData |  |
| 88 | `?GetTitleW@CLocation@@QEAAPEBGXZ` | `0x3DE0` | 43 | UnwindData |  |
| 89 | `?GetVersion@CCollection@@QEAAKXZ` | `0x3E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `?GetVisableRootFolder@CCollection@@QEAAPEAVCFolder@@XZ` | `0x3E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `?GetVolumeW@CLocation@@QEAAPEBGXZ` | `0x3E40` | 43 | UnwindData |  |
| 93 | `?HandleCollection@CCollection@@AEAAKPEAVCParseXML@@PEAD@Z` | `0x3F20` | 657 | UnwindData |  |
| 94 | `?HandleCollectionEntry@CCollection@@AEAAKPEAVCParseXML@@PEAD@Z` | `0x41C0` | 233 | UnwindData |  |
| 95 | `?HandleFolder@CCollection@@AEAAKPEAVCParseXML@@PEAD@Z` | `0x42B0` | 520 | UnwindData |  |
| 96 | `?HandleLocation@CCollection@@AEAAKPEAVCParseXML@@PEAD@Z` | `0x44C0` | 380 | UnwindData |  |
| 97 | `?HandleTitle@CCollection@@AEAAKPEAVCParseXML@@PEAD@Z` | `0x4650` | 1,305 | UnwindData |  |
| 98 | `?IncrementRefTitleCount@CCollection@@QEAAXXZ` | `0x4B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `?IsDirty@CCollection@@QEAAHXZ` | `0x4B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `?MergeKeywords@CCollection@@QEAAHPEAD@Z` | `0x4B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `?MergeKeywords@CCollection@@QEAAHPEAG@Z` | `0x4BA0` | 37 | UnwindData |  |
| 102 | `?NewLocation@CCollection@@AEAAPEAVCLocation@@XZ` | `0x4BD0` | 98 | UnwindData |  |
| 103 | `?NewLocationHistory@CTitle@@QEAAPEAULocationHistory@@XZ` | `0x4C40` | 97 | UnwindData |  |
| 104 | `?NewTitle@CCollection@@AEAAPEAVCTitle@@XZ` | `0x4CB0` | 86 | UnwindData |  |
| 105 | `?Next@CPointerList@@QEAAPEAUListItem@@PEAU2@@Z` | `0x4D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `?Open@CCollection@@QEAAKPEBD@Z` | `0x4D20` | 734 | UnwindData |  |
| 107 | `?Open@CCollection@@QEAAKPEBG@Z` | `0x5010` | 61 | UnwindData |  |
| 108 | `?ParseFile@CCollection@@AEAAKPEBD@Z` | `0x5060` | 1,353 | UnwindData |  |
| 109 | `?Release@CCollection@@AEAAKXZ` | `0x55B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `?RemoveAll@CPointerList@@QEAAXXZ` | `0x55D0` | 53 | UnwindData |  |
| 112 | `?RemoveCollection@CCollection@@QEAAKH@Z` | `0x5610` | 219 | UnwindData |  |
| 113 | `?RemoveCollectionEntry@CCollection@@QEAAXPEBD@Z` | `0x5700` | 167 | UnwindData |  |
| 114 | `?Save@CCollection@@QEAAKXZ` | `0x57B0` | 6,249 | UnwindData |  |
| 115 | `?SetExTitlePtr@CFolder@@QEAAXPEAVCExTitle@@@Z` | `0x7020` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `?SetFindMergedCHMS@CCollection@@QEAAXH@Z` | `0x7050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `?SetFirstChildFolder@CFolder@@QEAAXPEAV1@@Z` | `0x7060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `?SetId@CLocation@@QEAAXPEBD@Z` | `0x7070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `?SetId@CTitle@@QEAAXPEBD@Z` | `0x7070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `?SetTitle@CFolder@@QEAAXPEBD@Z` | `0x7070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `?SetId@CLocation@@QEAAXPEBG@Z` | `0x7090` | 55 | UnwindData |  |
| 121 | `?SetId@CTitle@@QEAAXPEBG@Z` | `0x7090` | 55 | UnwindData |  |
| 136 | `?SetTitle@CFolder@@QEAAXPEBG@Z` | `0x7090` | 55 | UnwindData |  |
| 122 | `?SetLanguage@CFolder@@QEAAXG@Z` | `0x70D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `?SetLanguage@CTitle@@QEAAXG@Z` | `0x70E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `?SetMasterCHM@CCollection@@QEAAXPEBDG@Z` | `0x70F0` | 45 | UnwindData |  |
| 125 | `?SetMasterCHM@CCollection@@QEAAXPEBGG@Z` | `0x7130` | 72 | UnwindData |  |
| 126 | `?SetNextFolder@CFolder@@QEAAXPEAV1@@Z` | `0x7180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `?SetNextLocation@CLocation@@QEAAXPEAV1@@Z` | `0x7190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `?SetNextTitle@CTitle@@QEAAXPEAV1@@Z` | `0x71A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `?SetOrder@CFolder@@QEAAXK@Z` | `0x71B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `?SetParent@CFolder@@QEAAXPEAV1@@Z` | `0x71C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `?SetPath@CLocation@@QEAAXPEBD@Z` | `0x71D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `?SetPath@CLocation@@QEAAXPEBG@Z` | `0x71F0` | 56 | UnwindData |  |
| 133 | `?SetSampleLocation@CCollection@@QEAAXPEBD@Z` | `0x7230` | 40 | UnwindData |  |
| 134 | `?SetSampleLocation@CCollection@@QEAAXPEBG@Z` | `0x7260` | 68 | UnwindData |  |
| 137 | `?SetTitle@CLocation@@QEAAXPEBD@Z` | `0x72B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `?SetTitle@CLocation@@QEAAXPEBG@Z` | `0x72D0` | 56 | UnwindData |  |
| 139 | `?SetVersion@CCollection@@QEAAXK@Z` | `0x7310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `?SetVolume@CLocation@@QEAAXPEBD@Z` | `0x7320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `?SetVolume@CLocation@@QEAAXPEBG@Z` | `0x7340` | 56 | UnwindData |  |
| 142 | `?WriteFolder@CCollection@@AEAAHPEAPEAVCFolder@@@Z` | `0x7400` | 1,579 | UnwindData |  |
| 143 | `?WriteFolders@CCollection@@AEAAHPEAPEAVCFolder@@@Z` | `0x7A40` | 112 | UnwindData |  |
| 144 | `?bIsVisable@CFolder@@QEAAHXZ` | `0x7AC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `?wssResetNextColNum@CCollection@@AEAAXXZ` | `0x7AE0` | 157 | UnwindData |  |
| 8 | `??1CFIFOString@@QEAA@XZ` | `0x8010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `?AddTail@CFIFOString@@QEAAKPEAD@Z` | `0x8020` | 143 | UnwindData |  |
| 84 | `?GetTail@CFIFOString@@QEAAKPEAPEAD@Z` | `0x8210` | 133 | UnwindData |  |
| 110 | `?RemoveAll@CFIFOString@@QEAAXXZ` | `0x85C0` | 64 | UnwindData |  |
