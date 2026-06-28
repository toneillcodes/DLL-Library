# Binary Specification: odbccp32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\odbccp32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b82e688f6d6a5246fb6290b740863682ccf32edf0b4928466aecc08378d5f3a4`
* **Total Exported Functions:** 57

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 215 | `SQLGetPrivateProfileStringW` | `0x1D30` | 4,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `SQLCreateDataSourceExW` | `0x2DC0` | 71 | UnwindData |  |
| 212 | `SQLCreateDataSourceW` | `0x2E10` | 240 | UnwindData |  |
| 222 | `SQLInstallerErrorW` | `0x5260` | 127 | UnwindData |  |
| 223 | `SQLPostInstallerErrorW` | `0x52F0` | 239 | UnwindData |  |
| 232 | `SQLLoadDataSourcesListBox` | `0x5B20` | 1,536 | UnwindData |  |
| 112 | `SelectTransDlg` | `0x6250` | 1,023 | UnwindData |  |
| 101 | `ODBCCPlApplet` | `0x7D20` | 138 | UnwindData |  |
| 206 | `SQLConfigDataSourceW` | `0x8EC0` | 118 | UnwindData |  |
| 221 | `SQLConfigDriverW` | `0x95F0` | 151 | UnwindData |  |
| 205 | `SQLGetAvailableDriversW` | `0x9740` | 65 | UnwindData |  |
| 27 | `SQLGetConfigMode` | `0x9790` | 94 | UnwindData |  |
| 204 | `SQLGetInstalledDriversW` | `0x9800` | 191 | UnwindData |  |
| 213 | `SQLGetTranslatorW` | `0x9A30` | 166 | UnwindData |  |
| 226 | `SQLInstallDriverExW` | `0x9C00` | 153 | UnwindData |  |
| 203 | `SQLInstallDriverManagerW` | `0x9CA0` | 158 | UnwindData |  |
| 202 | `SQLInstallDriverW` | `0x9D50` | 317 | UnwindData |  |
| 210 | `SQLInstallODBCW` | `0x9EA0` | 204 | UnwindData |  |
| 229 | `SQLInstallTranslatorExW` | `0xA120` | 65 | UnwindData |  |
| 218 | `SQLInstallTranslatorW` | `0xA170` | 164 | UnwindData |  |
| 11 | `SQLManageDataSources` | `0xA220` | 120 | UnwindData |  |
| 224 | `SQLReadFileDSNW` | `0xA2A0` | 147 | UnwindData |  |
| 209 | `SQLRemoveDSNFromIniW` | `0xA4F0` | 71 | UnwindData |  |
| 7 | `SQLRemoveDefaultDataSource` | `0xA540` | 238 | UnwindData |  |
| 17 | `SQLRemoveDriverManager` | `0xA730` | 75 | UnwindData |  |
| 220 | `SQLRemoveDriverW` | `0xA790` | 100 | UnwindData |  |
| 219 | `SQLRemoveTranslatorW` | `0xA8C0` | 86 | UnwindData |  |
| 28 | `SQLSetConfigMode` | `0xA920` | 132 | UnwindData |  |
| 216 | `SQLValidDSNW` | `0xAA40` | 66 | UnwindData |  |
| 208 | `SQLWriteDSNToIniW` | `0xAD30` | 86 | UnwindData |  |
| 225 | `SQLWriteFileDSNW` | `0xAD90` | 127 | UnwindData |  |
| 214 | `SQLWritePrivateProfileStringW` | `0xAF90` | 118 | UnwindData |  |
| 231 | `SQLLoadDriverListBox` | `0xE390` | 7,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SQLConfigDataSource` | `0x10130` | 172 | UnwindData |  |
| 21 | `SQLConfigDriver` | `0x101F0` | 344 | UnwindData |  |
| 12 | `SQLCreateDataSource` | `0x10350` | 83 | UnwindData |  |
| 30 | `SQLCreateDataSourceEx` | `0x103B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `SQLGetAvailableDrivers` | `0x103C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `SQLGetInstalledDrivers` | `0x103E0` | 216 | UnwindData |  |
| 15 | `SQLGetPrivateProfileString` | `0x104C0` | 417 | UnwindData |  |
| 13 | `SQLGetTranslator` | `0x10670` | 442 | UnwindData |  |
| 2 | `SQLInstallDriver` | `0x10830` | 297 | UnwindData |  |
| 26 | `SQLInstallDriverEx` | `0x10960` | 328 | UnwindData |  |
| 3 | `SQLInstallDriverManager` | `0x10AB0` | 172 | UnwindData |  |
| 10 | `SQLInstallODBC` | `0x10B70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `SQLInstallTranslator` | `0x10B90` | 378 | UnwindData |  |
| 29 | `SQLInstallTranslatorEx` | `0x10D10` | 65 | UnwindData |  |
| 22 | `SQLInstallerError` | `0x10D60` | 229 | UnwindData |  |
| 23 | `SQLPostInstallerError` | `0x10E50` | 101 | UnwindData |  |
| 24 | `SQLReadFileDSN` | `0x10EC0` | 384 | UnwindData |  |
| 9 | `SQLRemoveDSNFromIni` | `0x11050` | 62 | UnwindData |  |
| 20 | `SQLRemoveDriver` | `0x110A0` | 90 | UnwindData |  |
| 19 | `SQLRemoveTranslator` | `0x11100` | 77 | UnwindData |  |
| 16 | `SQLValidDSN` | `0x11160` | 99 | UnwindData |  |
| 8 | `SQLWriteDSNToIni` | `0x111D0` | 132 | UnwindData |  |
| 25 | `SQLWriteFileDSN` | `0x11260` | 273 | UnwindData |  |
| 14 | `SQLWritePrivateProfileString` | `0x11380` | 222 | UnwindData |  |
