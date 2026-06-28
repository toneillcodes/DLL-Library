# Binary Specification: certadm.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\certadm.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bc9d35419dc4c224078336324c15137410a684cbeee66e12e358c74c02cc54d2`
* **Total Exported Functions:** 49

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `CertSrvBackupClose` | `0x54B0` | 212 | UnwindData |  |
| 6 | `CertSrvBackupEnd` | `0x5590` | 201 | UnwindData |  |
| 15 | `CertSrvBackupFree` | `0x5660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `CertSrvBackupGetBackupLogsW` | `0x5680` | 59 | UnwindData |  |
| 8 | `CertSrvBackupGetDatabaseNamesW` | `0x56D0` | 56 | UnwindData |  |
| 14 | `CertSrvBackupGetDynamicFileListW` | `0x5710` | 59 | UnwindData |  |
| 9 | `CertSrvBackupOpenFileW` | `0x5760` | 349 | UnwindData |  |
| 10 | `CertSrvBackupPrepareW` | `0x58D0` | 498 | UnwindData |  |
| 11 | `CertSrvBackupRead` | `0x5AD0` | 537 | UnwindData |  |
| 12 | `CertSrvBackupTruncateLogs` | `0x5CF0` | 174 | UnwindData |  |
| 13 | `CertSrvIsServerOnlineW` | `0x5DB0` | 376 | UnwindData |  |
| 23 | `CAClosePerfMon` | `0x7FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `CACollectPerfMon` | `0x7FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `CAOpenPerfMon` | `0x7FD0` | 3,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `DllUnregisterServer` | `0x8EE0` | 16,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `OpenPerfMon` | `0x8EE0` | 16,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `DllCanUnloadNow` | `0xCE50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `DllGetClassObject` | `0xCE70` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `DllRegisterServer` | `0xCFD0` | 216 | UnwindData |  |
| 210 | *Ordinal Only* | `0xD1A0` | 152 | UnwindData |  |
| 211 | *Ordinal Only* | `0xD240` | 147 | UnwindData |  |
| 212 | *Ordinal Only* | `0xF460` | 356 | UnwindData |  |
| 213 | *Ordinal Only* | `0xFB10` | 192 | UnwindData |  |
| 216 | *Ordinal Only* | `0xFED0` | 806 | UnwindData |  |
| 217 | *Ordinal Only* | `0x10200` | 129 | UnwindData |  |
| 222 | *Ordinal Only* | `0x13320` | 201 | UnwindData |  |
| 215 | *Ordinal Only* | `0x133F0` | 181 | UnwindData |  |
| 21 | `CertSrvRestoreEnd` | `0x20420` | 128 | UnwindData |  |
| 17 | `CertSrvRestoreGetDatabaseLocationsW` | `0x204B0` | 227 | UnwindData |  |
| 18 | `CertSrvRestorePrepareW` | `0x205A0` | 194 | UnwindData |  |
| 20 | `CertSrvRestoreRegisterComplete` | `0x20670` | 378 | UnwindData |  |
| 22 | `CertSrvRestoreRegisterThroughFile` | `0x207F0` | 1,814 | UnwindData |  |
| 19 | `CertSrvRestoreRegisterW` | `0x20F10` | 1,574 | UnwindData |  |
| 16 | `CertSrvServerControlW` | `0x21540` | 530 | UnwindData |  |
| 218 | *Ordinal Only* | `0x23C50` | 1,211 | UnwindData |  |
| 220 | *Ordinal Only* | `0x24120` | 1,181 | UnwindData |  |
| 221 | *Ordinal Only* | `0x245D0` | 1,578 | UnwindData |  |
| 219 | *Ordinal Only* | `0x27E70` | 1,736 | UnwindData |  |
| 26 | `ClosePerfMon` | `0x391F0` | 62 | UnwindData |  |
| 203 | *Ordinal Only* | `0x39240` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | *Ordinal Only* | `0x39270` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | *Ordinal Only* | `0x392A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | *Ordinal Only* | `0x392D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | *Ordinal Only* | `0x392F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | *Ordinal Only* | `0x39320` | 264 | UnwindData |  |
| 205 | *Ordinal Only* | `0x39430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | *Ordinal Only* | `0x39450` | 121 | UnwindData |  |
| 208 | *Ordinal Only* | `0x394D0` | 8,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `CollectPerfMon` | `0x3B710` | 144 | UnwindData |  |
