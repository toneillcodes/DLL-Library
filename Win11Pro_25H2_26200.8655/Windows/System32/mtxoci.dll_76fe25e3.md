# Binary Specification: mtxoci.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mtxoci.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `76fe25e3681c979eabf05a036bb8acef2d4a02ffb3be4a4a92e2d271367b97fe`
* **Total Exported Functions:** 40

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1006 | `MTxOciRegisterCursor` | `0x2310` | 281 | UnwindData |  |
| 37 | `obindps` | `0x2430` | 390 | UnwindData |  |
| 1 | `obndra` | `0x25C0` | 320 | UnwindData |  |
| 2 | `obndrn` | `0x2710` | 247 | UnwindData |  |
| 3 | `obndrv` | `0x2810` | 259 | UnwindData |  |
| 4 | `obreak` | `0x2920` | 154 | UnwindData |  |
| 5 | `ocan` | `0x29C0` | 127 | UnwindData |  |
| 6 | `oclose` | `0x2A50` | 416 | UnwindData |  |
| 7 | `ocof` | `0x2C00` | 138 | UnwindData |  |
| 8 | `ocom` | `0x2C90` | 138 | UnwindData |  |
| 9 | `ocon` | `0x2D20` | 138 | UnwindData |  |
| 10 | `odefin` | `0x2DB0` | 283 | UnwindData |  |
| 38 | `odefinps` | `0x2EE0` | 344 | UnwindData |  |
| 11 | `odescr` | `0x3040` | 256 | UnwindData |  |
| 12 | `odessp` | `0x3150` | 702 | UnwindData |  |
| 13 | `oerhms` | `0x3420` | 276 | UnwindData |  |
| 14 | `oermsg` | `0x3540` | 52 | UnwindData |  |
| 15 | `oexec` | `0x3580` | 127 | UnwindData |  |
| 16 | `oexfet` | `0x3610` | 163 | UnwindData |  |
| 17 | `oexn` | `0x36C0` | 160 | UnwindData |  |
| 18 | `ofen` | `0x3770` | 141 | UnwindData |  |
| 19 | `ofetch` | `0x3810` | 127 | UnwindData |  |
| 20 | `oflng` | `0x38A0` | 203 | UnwindData |  |
| 39 | `ogetpi` | `0x3980` | 176 | UnwindData |  |
| 26 | `oopen` | `0x3A40` | 466 | UnwindData |  |
| 27 | `oopt` | `0x3C20` | 160 | UnwindData |  |
| 28 | `oparse` | `0x3CD0` | 174 | UnwindData |  |
| 29 | `orol` | `0x3D90` | 154 | UnwindData |  |
| 40 | `osetpi` | `0x3E30` | 163 | UnwindData |  |
| 1005 | `MTxOciGetVersion` | `0x3EE0` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1001 | `Enlist` | `0x4130` | 282 | UnwindData |  |
| 1003 | `MTxOciInit` | `0x4250` | 159 | UnwindData |  |
| 1004 | `MTxolog` | `0x4300` | 570 | UnwindData |  |
| 21 | `olog` | `0x4540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1000 | `ologTransacted` | `0x4550` | 331 | UnwindData |  |
| 22 | `ologof` | `0x46B0` | 518 | UnwindData |  |
| 41 | `opinit` | `0x48C0` | 159 | UnwindData |  |
| 24 | `DllUnregisterServer` | `0x6780` | 25,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `DllRegisterServer` | `0xCAE0` | 285 | UnwindData |  |
| 1002 | `GetXaSwitch` | `0xD5A0` | 26,077 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
