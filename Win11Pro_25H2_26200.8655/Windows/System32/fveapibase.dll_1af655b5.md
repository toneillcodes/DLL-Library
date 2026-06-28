# Binary Specification: fveapibase.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\fveapibase.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1af655b5b97f2158f87844de22734d52d1f6c44eb5899ed97123c7f215bf7aa3`
* **Total Exported Functions:** 63

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `InternalFveIsVolumeEncrypted` | `0x7640` | 227 | UnwindData |  |
| 2 | `FveAuthElementFromPassPhraseW` | `0x9D40` | 165 | UnwindData |  |
| 3 | `FveAuthElementFromPinW` | `0x9DF0` | 191 | UnwindData |  |
| 4 | `FveAuthElementFromRecoveryPasswordW` | `0x9EC0` | 165 | UnwindData |  |
| 5 | `FveAuthElementGetKeyFileNameW` | `0x9F70` | 188 | UnwindData |  |
| 6 | `FveAuthElementReadExternalKeyW` | `0xA040` | 208 | UnwindData |  |
| 7 | `FveAuthElementToRecoveryPasswordW` | `0xA120` | 188 | UnwindData |  |
| 8 | `FveAuthElementWriteExternalKeyExW` | `0xA1F0` | 188 | UnwindData |  |
| 9 | `FveAuthElementWriteExternalKeyW` | `0xA2C0` | 178 | UnwindData |  |
| 10 | `FveCanPinExceptionPolicyBeApplied` | `0xA380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `FveClearRecoveryPasswordBackupInformation` | `0xA390` | 218 | UnwindData |  |
| 12 | `FveClearUserFlags` | `0xA470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `FveGetUserFlags` | `0xA470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `FveSetUserFlags` | `0xA470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `FveCloseHandle` | `0xA480` | 177 | UnwindData |  |
| 14 | `FveCloseVolume` | `0xA540` | 166 | UnwindData |  |
| 15 | `FveCommitChanges` | `0xA5F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `FveCommitChangesEx` | `0xA600` | 277 | UnwindData |  |
| 17 | `FveConversionDecrypt` | `0xA720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `FveConversionDecryptEx` | `0xA730` | 220 | UnwindData |  |
| 19 | `FveConversionPause` | `0xA820` | 204 | UnwindData |  |
| 20 | `FveConversionResume` | `0xA900` | 204 | UnwindData |  |
| 21 | `FveConversionStop` | `0xA9E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `FveConversionStopEx` | `0xA9F0` | 222 | UnwindData |  |
| 23 | `FveDiscardChanges` | `0xAAE0` | 186 | UnwindData |  |
| 24 | `FveEnableRawAccess` | `0xABA0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `FveEraseDrive` | `0xAC70` | 200 | UnwindData |  |
| 26 | `FveFindFirstVolume` | `0xAD40` | 275 | UnwindData |  |
| 27 | `FveFindNextVolume` | `0xAE60` | 228 | UnwindData |  |
| 28 | `FveGetAllowKeyExport` | `0xAF50` | 177 | UnwindData |  |
| 29 | `FveGetAuthMethodGuids` | `0xB010` | 237 | UnwindData |  |
| 30 | `FveGetAuthMethodInformation` | `0xB110` | 238 | UnwindData |  |
| 31 | `FveGetDataSet` | `0xB210` | 233 | UnwindData |  |
| 32 | `FveGetDataSetEx` | `0xB300` | 245 | UnwindData |  |
| 33 | `FveGetFipsAllowDisabled` | `0xB400` | 152 | UnwindData |  |
| 34 | `FveGetFveMethod` | `0xB4A0` | 195 | UnwindData |  |
| 35 | `FveGetFveMethodEDrv` | `0xB570` | 213 | UnwindData |  |
| 36 | `FveGetFveMethodEx` | `0xB650` | 255 | UnwindData |  |
| 37 | `FveGetIdentity` | `0xB760` | 201 | UnwindData |  |
| 38 | `FveGetKeyPackage` | `0xB830` | 255 | UnwindData |  |
| 39 | `FveGetRecoveryPasswordBackupAccountInformation` | `0xB940` | 238 | UnwindData |  |
| 40 | `FveGetStatus` | `0xBA40` | 230 | UnwindData |  |
| 41 | `FveGetStatusW` | `0xBB30` | 657 | UnwindData |  |
| 43 | `FveGetVolumeNameW` | `0xBDD0` | 691 | UnwindData |  |
| 44 | `FveIsHardwareReadyForConversion` | `0xC090` | 120 | UnwindData |  |
| 45 | `FveIsRecoveryPasswordGroupValidW` | `0xC110` | 165 | UnwindData |  |
| 46 | `FveIsRecoveryPasswordValidW` | `0xC1C0` | 165 | UnwindData |  |
| 47 | `FveIsVolumeEncryptable` | `0xC270` | 167 | UnwindData |  |
| 48 | `FveLockVolume` | `0xC320` | 200 | UnwindData |  |
| 49 | `FveNotifyVolumeAfterFormat` | `0xC3F0` | 167 | UnwindData |  |
| 50 | `FveOpenVolumeByHandle` | `0xC4A0` | 572 | UnwindData |  |
| 54 | `FveRevertVolume` | `0xC6F0` | 167 | UnwindData |  |
| 55 | `FveSelectBestRecoveryPasswordByBackupInformation` | `0xC7A0` | 183 | UnwindData |  |
| 56 | `FveSetAllowKeyExport` | `0xC860` | 201 | UnwindData |  |
| 57 | `FveSetFipsAllowDisabled` | `0xC930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `FveSetFveMethod` | `0xC940` | 181 | UnwindData |  |
| 59 | `FveSetFveMethodEx` | `0xCA00` | 216 | UnwindData |  |
| 60 | `FveSetRecoveryPasswordBackupAccountInformation` | `0xCAE0` | 228 | UnwindData |  |
| 61 | `FveSetRecoveryPasswordBackupInformation` | `0xCBD0` | 240 | UnwindData |  |
| 63 | `FveUpgradeVolume` | `0xCCD0` | 167 | UnwindData |  |
| 51 | `FveOpenVolumeExW` | `0xDBA0` | 259 | UnwindData |  |
| 52 | `FveOpenVolumeW` | `0xDCB0` | 34 | UnwindData |  |
| 53 | `FveQuery` | `0xDCE0` | 510,240 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
