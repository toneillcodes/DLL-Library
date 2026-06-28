# Binary Specification: WMVCORE.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WMVCORE.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `331a50d7363836dc7b60593270f0a3f147b43dba5e54bb7e332e77c4adc75797`
* **Total Exported Functions:** 21

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `WMCreateEditor` | `0x257D0` | 124 | UnwindData |  |
| 8 | `DllRegisterServer` | `0x32FD0` | 589 | UnwindData |  |
| 13 | `WMCreateReader` | `0x38210` | 122 | UnwindData |  |
| 14 | `WMCreateReaderPriv` | `0x38290` | 148 | UnwindData |  |
| 21 | `WMIsContentProtected` | `0x38330` | 157 | UnwindData |  |
| 9 | `WMCreateBackupRestorer` | `0x38F70` | 37,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `WMCreateBackupRestorerPrivate` | `0x38F70` | 37,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `WMCreateLicenseRevocationAgentPrivate` | `0x38F70` | 37,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `WMCreateSyncReaderPriv` | `0x42340` | 134 | UnwindData |  |
| 15 | `WMCreateSyncReader` | `0x423D0` | 111 | UnwindData |  |
| 1 | `WMCheckURLExtension` | `0x45260` | 165 | UnwindData |  |
| 2 | `WMCheckURLScheme` | `0x45310` | 113 | UnwindData |  |
| 7 | `WMValidateData` | `0x45670` | 322 | UnwindData |  |
| 6 | `WMIsAvailableOffline` | `0x54E70` | 499 | UnwindData |  |
| 16 | `WMCreateWriter` | `0x9EEF0` | 99 | UnwindData |  |
| 19 | `WMCreateWriterPriv` | `0x9EF60` | 130 | UnwindData |  |
| 17 | `WMCreateWriterFileSink` | `0xBA0F0` | 152 | UnwindData |  |
| 18 | `WMCreateWriterNetworkSink` | `0xBD380` | 154 | UnwindData |  |
| 20 | `WMCreateWriterPushSink` | `0xCB4D0` | 138 | UnwindData |  |
| 12 | `WMCreateProfileManager` | `0xE9FE0` | 88 | UnwindData |  |
| 11 | `WMCreateIndexer` | `0x10B3A0` | 124 | UnwindData |  |
