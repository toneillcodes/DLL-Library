# Binary Specification: mtxoci.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mtxoci.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fbbdeb2e91910413e94c5de2b4115ac969c1f41ad7e3deb3bf8f7a77af2a1058`
* **Total Exported Functions:** 40

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1006 | `MTxOciRegisterCursor` | `0x2510` | 281 | UnwindData |  |
| 37 | `obindps` | `0x2630` | 390 | UnwindData |  |
| 1 | `obndra` | `0x27C0` | 320 | UnwindData |  |
| 2 | `obndrn` | `0x2910` | 247 | UnwindData |  |
| 3 | `obndrv` | `0x2A10` | 259 | UnwindData |  |
| 4 | `obreak` | `0x2B20` | 154 | UnwindData |  |
| 5 | `ocan` | `0x2BC0` | 127 | UnwindData |  |
| 6 | `oclose` | `0x2C50` | 416 | UnwindData |  |
| 7 | `ocof` | `0x2E00` | 138 | UnwindData |  |
| 8 | `ocom` | `0x2E90` | 138 | UnwindData |  |
| 9 | `ocon` | `0x2F20` | 138 | UnwindData |  |
| 10 | `odefin` | `0x2FB0` | 283 | UnwindData |  |
| 38 | `odefinps` | `0x30E0` | 344 | UnwindData |  |
| 11 | `odescr` | `0x3240` | 256 | UnwindData |  |
| 12 | `odessp` | `0x3350` | 702 | UnwindData |  |
| 13 | `oerhms` | `0x3620` | 276 | UnwindData |  |
| 14 | `oermsg` | `0x3740` | 52 | UnwindData |  |
| 15 | `oexec` | `0x3780` | 127 | UnwindData |  |
| 16 | `oexfet` | `0x3810` | 163 | UnwindData |  |
| 17 | `oexn` | `0x38C0` | 160 | UnwindData |  |
| 18 | `ofen` | `0x3970` | 141 | UnwindData |  |
| 19 | `ofetch` | `0x3A10` | 127 | UnwindData |  |
| 20 | `oflng` | `0x3AA0` | 203 | UnwindData |  |
| 39 | `ogetpi` | `0x3B80` | 176 | UnwindData |  |
| 26 | `oopen` | `0x3C40` | 466 | UnwindData |  |
| 27 | `oopt` | `0x3E20` | 160 | UnwindData |  |
| 28 | `oparse` | `0x3ED0` | 174 | UnwindData |  |
| 29 | `orol` | `0x3F90` | 154 | UnwindData |  |
| 40 | `osetpi` | `0x4030` | 163 | UnwindData |  |
| 1005 | `MTxOciGetVersion` | `0x40E0` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1001 | `Enlist` | `0x4330` | 282 | UnwindData |  |
| 1003 | `MTxOciInit` | `0x4450` | 159 | UnwindData |  |
| 1004 | `MTxolog` | `0x4500` | 570 | UnwindData |  |
| 21 | `olog` | `0x4740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1000 | `ologTransacted` | `0x4750` | 331 | UnwindData |  |
| 22 | `ologof` | `0x48B0` | 518 | UnwindData |  |
| 41 | `opinit` | `0x4AC0` | 159 | UnwindData |  |
| 24 | `DllUnregisterServer` | `0x6980` | 25,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `DllRegisterServer` | `0xCCE0` | 285 | UnwindData |  |
| 1002 | `GetXaSwitch` | `0xD7A0` | 53,293 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
