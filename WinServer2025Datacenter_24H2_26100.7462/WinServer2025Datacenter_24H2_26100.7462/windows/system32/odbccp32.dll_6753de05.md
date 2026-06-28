# Binary Specification: odbccp32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\odbccp32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6753de05f7060fb2bab2c908edff9cdaedf4dd43e212a6edda7bb1172d18bbbb`
* **Total Exported Functions:** 57

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 215 | `SQLGetPrivateProfileStringW` | `0x1D30` | 25,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `SQLCreateDataSourceExW` | `0x80D0` | 71 | UnwindData |  |
| 212 | `SQLCreateDataSourceW` | `0x8120` | 240 | UnwindData |  |
| 222 | `SQLInstallerErrorW` | `0xA330` | 127 | UnwindData |  |
| 223 | `SQLPostInstallerErrorW` | `0xA3C0` | 239 | UnwindData |  |
| 232 | `SQLLoadDataSourcesListBox` | `0xABF0` | 1,536 | UnwindData |  |
| 112 | `SelectTransDlg` | `0xB320` | 1,023 | UnwindData |  |
| 101 | `ODBCCPlApplet` | `0xCDF0` | 138 | UnwindData |  |
| 206 | `SQLConfigDataSourceW` | `0xDF90` | 118 | UnwindData |  |
| 221 | `SQLConfigDriverW` | `0xE6C0` | 151 | UnwindData |  |
| 205 | `SQLGetAvailableDriversW` | `0xE810` | 65 | UnwindData |  |
| 27 | `SQLGetConfigMode` | `0xE860` | 94 | UnwindData |  |
| 204 | `SQLGetInstalledDriversW` | `0xE8D0` | 191 | UnwindData |  |
| 213 | `SQLGetTranslatorW` | `0xEB00` | 166 | UnwindData |  |
| 226 | `SQLInstallDriverExW` | `0xECD0` | 153 | UnwindData |  |
| 203 | `SQLInstallDriverManagerW` | `0xED70` | 158 | UnwindData |  |
| 202 | `SQLInstallDriverW` | `0xEE20` | 317 | UnwindData |  |
| 210 | `SQLInstallODBCW` | `0xEF70` | 204 | UnwindData |  |
| 229 | `SQLInstallTranslatorExW` | `0xF1F0` | 65 | UnwindData |  |
| 218 | `SQLInstallTranslatorW` | `0xF240` | 164 | UnwindData |  |
| 11 | `SQLManageDataSources` | `0xF2F0` | 120 | UnwindData |  |
| 224 | `SQLReadFileDSNW` | `0xF370` | 147 | UnwindData |  |
| 209 | `SQLRemoveDSNFromIniW` | `0xF5C0` | 71 | UnwindData |  |
| 7 | `SQLRemoveDefaultDataSource` | `0xF610` | 238 | UnwindData |  |
| 17 | `SQLRemoveDriverManager` | `0xF800` | 75 | UnwindData |  |
| 220 | `SQLRemoveDriverW` | `0xF860` | 100 | UnwindData |  |
| 219 | `SQLRemoveTranslatorW` | `0xF990` | 86 | UnwindData |  |
| 28 | `SQLSetConfigMode` | `0xF9F0` | 132 | UnwindData |  |
| 216 | `SQLValidDSNW` | `0xFB10` | 66 | UnwindData |  |
| 208 | `SQLWriteDSNToIniW` | `0xFE00` | 86 | UnwindData |  |
| 225 | `SQLWriteFileDSNW` | `0xFE60` | 127 | UnwindData |  |
| 214 | `SQLWritePrivateProfileStringW` | `0x10060` | 118 | UnwindData |  |
| 231 | `SQLLoadDriverListBox` | `0x13470` | 7,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SQLConfigDataSource` | `0x15210` | 172 | UnwindData |  |
| 21 | `SQLConfigDriver` | `0x152D0` | 344 | UnwindData |  |
| 12 | `SQLCreateDataSource` | `0x15430` | 83 | UnwindData |  |
| 30 | `SQLCreateDataSourceEx` | `0x15490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `SQLGetAvailableDrivers` | `0x154A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `SQLGetInstalledDrivers` | `0x154C0` | 216 | UnwindData |  |
| 15 | `SQLGetPrivateProfileString` | `0x155A0` | 417 | UnwindData |  |
| 13 | `SQLGetTranslator` | `0x15750` | 442 | UnwindData |  |
| 2 | `SQLInstallDriver` | `0x15910` | 297 | UnwindData |  |
| 26 | `SQLInstallDriverEx` | `0x15A40` | 328 | UnwindData |  |
| 3 | `SQLInstallDriverManager` | `0x15B90` | 172 | UnwindData |  |
| 10 | `SQLInstallODBC` | `0x15C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `SQLInstallTranslator` | `0x15C70` | 378 | UnwindData |  |
| 29 | `SQLInstallTranslatorEx` | `0x15DF0` | 65 | UnwindData |  |
| 22 | `SQLInstallerError` | `0x15E40` | 229 | UnwindData |  |
| 23 | `SQLPostInstallerError` | `0x15F30` | 101 | UnwindData |  |
| 24 | `SQLReadFileDSN` | `0x15FA0` | 384 | UnwindData |  |
| 9 | `SQLRemoveDSNFromIni` | `0x16130` | 62 | UnwindData |  |
| 20 | `SQLRemoveDriver` | `0x16180` | 90 | UnwindData |  |
| 19 | `SQLRemoveTranslator` | `0x161E0` | 77 | UnwindData |  |
| 16 | `SQLValidDSN` | `0x16240` | 99 | UnwindData |  |
| 8 | `SQLWriteDSNToIni` | `0x162B0` | 132 | UnwindData |  |
| 25 | `SQLWriteFileDSN` | `0x16340` | 273 | UnwindData |  |
| 14 | `SQLWritePrivateProfileString` | `0x16460` | 222 | UnwindData |  |
