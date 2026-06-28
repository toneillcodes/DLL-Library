# Binary Specification: WMVCORE.DLL

## Binary Metadata
* **Original Path:** `c:\windows\system32\WMVCORE.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `aed73e6c08a738dd8ab8b60ba982ae1b966ba435432102d052e33945045ae32b`
* **Total Exported Functions:** 21

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `WMCreateEditor` | `0x25790` | 124 | UnwindData |  |
| 8 | `DllRegisterServer` | `0x32700` | 589 | UnwindData |  |
| 13 | `WMCreateReader` | `0x37930` | 122 | UnwindData |  |
| 14 | `WMCreateReaderPriv` | `0x379B0` | 148 | UnwindData |  |
| 21 | `WMIsContentProtected` | `0x37A50` | 157 | UnwindData |  |
| 9 | `WMCreateBackupRestorer` | `0x38690` | 37,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `WMCreateBackupRestorerPrivate` | `0x38690` | 37,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `WMCreateLicenseRevocationAgentPrivate` | `0x38690` | 37,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `WMCreateSyncReaderPriv` | `0x41A50` | 134 | UnwindData |  |
| 15 | `WMCreateSyncReader` | `0x41AE0` | 111 | UnwindData |  |
| 1 | `WMCheckURLExtension` | `0x44970` | 165 | UnwindData |  |
| 2 | `WMCheckURLScheme` | `0x44A20` | 113 | UnwindData |  |
| 7 | `WMValidateData` | `0x44D80` | 322 | UnwindData |  |
| 6 | `WMIsAvailableOffline` | `0x545C0` | 499 | UnwindData |  |
| 16 | `WMCreateWriter` | `0x9A380` | 99 | UnwindData |  |
| 19 | `WMCreateWriterPriv` | `0x9A3F0` | 130 | UnwindData |  |
| 17 | `WMCreateWriterFileSink` | `0xB5310` | 152 | UnwindData |  |
| 18 | `WMCreateWriterNetworkSink` | `0xB8560` | 154 | UnwindData |  |
| 20 | `WMCreateWriterPushSink` | `0xC6A00` | 138 | UnwindData |  |
| 12 | `WMCreateProfileManager` | `0xE5380` | 88 | UnwindData |  |
| 11 | `WMCreateIndexer` | `0x1066D0` | 124 | UnwindData |  |
