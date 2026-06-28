# Binary Specification: rgb9rast.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\rgb9rast.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e18bdbb55534bd4f84b6ab9aa4fcf1eb5b75e4e511676324cae6c147b36b8014`
* **Total Exported Functions:** 30

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `??4PrimProcessor@@QEAAAEAV0@AEBV0@@Z` | `0x21B0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `?ClrFlags@PrimProcessor@@QEAAXI@Z` | `0x2260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `?GetFlags@PrimProcessor@@QEAAIXZ` | `0x2270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `?SetFlags@PrimProcessor@@QEAAXI@Z` | `0x2280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `?StateChanged@PrimProcessor@@QEAAXXZ` | `0x2290` | 24,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `D3D9GetSWInfo` | `0x8110` | 156 | UnwindData |  |
| 1 | `??0PrimProcessor@@QEAA@XZ` | `0x8260` | 60 | UnwindData |  |
| 2 | `??1PrimProcessor@@QEAA@XZ` | `0x82B0` | 39 | UnwindData |  |
| 4 | `?AllocSpans@PrimProcessor@@QEAAJPEAIPEAPEAUtagD3DI_RASTSPAN@@@Z` | `0x82E0` | 172 | UnwindData |  |
| 5 | `?AppendPrim@PrimProcessor@@AEAAJXZ` | `0x83A0` | 161 | UnwindData |  |
| 6 | `?Begin@PrimProcessor@@QEAAXXZ` | `0x8450` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `?End@PrimProcessor@@QEAAJXZ` | `0x8480` | 45 | UnwindData |  |
| 11 | `?Flush@PrimProcessor@@AEAAJXZ` | `0x84C0` | 99 | UnwindData |  |
| 12 | `?FlushPartial@PrimProcessor@@AEAAJXZ` | `0x8530` | 352 | UnwindData |  |
| 13 | `?FreeSpans@PrimProcessor@@QEAAXI@Z` | `0x86A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `?Initialize@PrimProcessor@@QEAAJXZ` | `0x86C0` | 84 | UnwindData |  |
| 23 | `?ResetBuffer@PrimProcessor@@AEAAXXZ` | `0x8720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `?SetCtx@PrimProcessor@@QEAAXPEAUtagD3DI_RASTCTX@@@Z` | `0x8740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `?BeginPrimSet@PrimProcessor@@QEAAXW4_D3DPRIMITIVETYPE@@W4_RAST_VERTEX_TYPE@@@Z` | `0x8750` | 786 | UnwindData |  |
| 10 | `?FillPointSpan@PrimProcessor@@AEAAXPEAU_D3DTLVERTEX@@PEAUtagD3DI_RASTSPAN@@@Z` | `0x8A70` | 690 | UnwindData |  |
| 19 | `?NormalizePointRHW@PrimProcessor@@AEAAXPEAU_D3DTLVERTEX@@@Z` | `0x8D30` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `?Point@PrimProcessor@@QEAAJPEAU_D3DTLVERTEX@@0@Z` | `0x8D70` | 321 | UnwindData |  |
| 16 | `?Line@PrimProcessor@@QEAAJPEAU_D3DTLVERTEX@@00@Z` | `0x8EC0` | 209 | UnwindData |  |
| 17 | `?LineSetup@PrimProcessor@@AEAAHPEAU_D3DTLVERTEX@@0@Z` | `0x9290` | 1,425 | UnwindData |  |
| 18 | `?NormalizeLineRHW@PrimProcessor@@AEAAXPEAU_D3DTLVERTEX@@0@Z` | `0xA070` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `?PointDiamondCheck@PrimProcessor@@AEAAHHHHH@Z` | `0xA0C0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `?NormalizeTriRHW@PrimProcessor@@AEAAXPEAU_D3DTLVERTEX@@00@Z` | `0xA140` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `?TriSetup@PrimProcessor@@AEAAHPEAU_D3DTLVERTEX@@00@Z` | `0xA1D0` | 2,010 | UnwindData |  |
| 26 | `?SetTriFunctions@PrimProcessor@@AEAAXXZ` | `0xA9B0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `?Tri@PrimProcessor@@QEAAJPEAU_D3DTLVERTEX@@00@Z` | `0xAA50` | 409 | UnwindData |  |
