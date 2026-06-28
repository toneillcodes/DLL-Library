# Binary Specification: vssapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vssapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `22172a6ebf7d714662d8f8b5bd6c784b81f53cb70a3d3b51b881e439d5305e7b`
* **Total Exported Functions:** 84

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 15 | `?CreateVssExamineWriterMetadata@@YAJPEAGPEAPEAVIVssExamineWriterMetadata@@@Z` | `0x1E9F0` | 1,029 | UnwindData |  |
| 76 | `CreateVssExamineWriterMetadataInternal` | `0x1E9F0` | 1,029 | UnwindData |  |
| 79 | `CreateWriter` | `0x3E570` | 228 | UnwindData |  |
| 6 | `VssFreeSnapshotProperties` | `0x43750` | 291 | UnwindData |  |
| 88 | `VssFreeSnapshotPropertiesInternal` | `0x43750` | 291 | UnwindData |  |
| 14 | `?CreateVssBackupComponents@@YAJPEAPEAVIVssBackupComponents@@@Z` | `0x49870` | 487 | UnwindData |  |
| 75 | `CreateVssBackupComponentsInternal` | `0x49870` | 487 | UnwindData |  |
| 81 | `DllCanUnloadNow` | `0x4AB30` | 20,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `CreateWriterEx` | `0x4FCF0` | 236 | UnwindData |  |
| 82 | `DllGetClassObject` | `0x59080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `GetProviderMgmtInterface` | `0x590A0` | 1,077 | UnwindData |  |
| 84 | `GetProviderMgmtInterfaceInternal` | `0x590A0` | 1,077 | UnwindData |  |
| 5 | `IsVolumeSnapshotted` | `0x594E0` | 3,046 | UnwindData |  |
| 85 | `IsVolumeSnapshottedInternal` | `0x594E0` | 3,046 | UnwindData |  |
| 7 | `ShouldBlockRevert` | `0x5A0D0` | 3,664 | UnwindData |  |
| 87 | `ShouldBlockRevertInternal` | `0x5A0D0` | 3,664 | UnwindData |  |
| 9 | `??0CVssWriter@@QEAA@XZ` | `0x5B590` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??1CVssWriter@@UEAA@XZ` | `0x5B890` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `?AreComponentsSelected@CVssWriter@@IEBA_NXZ` | `0x5BCA0` | 33 | UnwindData |  |
| 17 | `?GetBackupType@CVssWriter@@IEBA?AW4_VSS_BACKUP_TYPE@@XZ` | `0x5C110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `?GetContext@CVssWriter@@IEBAJXZ` | `0x5C120` | 33 | UnwindData |  |
| 21 | `?GetCurrentLevel@CVssWriter@@IEBA?AW4_VSS_APPLICATION_LEVEL@@XZ` | `0x5C290` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `?GetCurrentSnapshotSetId@CVssWriter@@IEBA?AU_GUID@@XZ` | `0x5C330` | 24 | UnwindData |  |
| 25 | `?GetCurrentVolumeArray@CVssWriter@@IEBAPEAPEBGXZ` | `0x5C350` | 33 | UnwindData |  |
| 27 | `?GetCurrentVolumeCount@CVssWriter@@IEBAIXZ` | `0x5C380` | 33 | UnwindData |  |
| 29 | `?GetRestoreType@CVssWriter@@IEBA?AW4_VSS_RESTORE_TYPE@@XZ` | `0x5C980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `?GetSnapshotDeviceName@CVssWriter@@IEBAJPEBGPEAPEBG@Z` | `0x5C990` | 2,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `?Initialize@CVssWriter@@QEAAJU_GUID@@PEBGW4VSS_USAGE_TYPE@@W4VSS_SOURCE_TYPE@@W4_VSS_APPLICATION_LEVEL@@KW4VSS_ALTERNATE_WRITER_STATE@@_N1@Z` | `0x5D230` | 97 | UnwindData |  |
| 34 | `?InstallAlternateWriter@CVssWriter@@QEAAJU_GUID@@0@Z` | `0x5D2A0` | 70 | UnwindData |  |
| 36 | `?IsBootableSystemStateBackedUp@CVssWriter@@IEBA_NXZ` | `0x5D380` | 33 | UnwindData |  |
| 38 | `?IsPartialFileSupportEnabled@CVssWriter@@IEBA_NXZ` | `0x5D3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `?IsPathAffected@CVssWriter@@IEBA_NPEBG@Z` | `0x5D3E0` | 33 | UnwindData |  |
| 43 | `?OnBackOffIOOnVolume@CVssWriter@@UEAA_NPEAGU_GUID@@1@Z` | `0x5DB90` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `?OnBackupComplete@CVssWriter@@UEAA_NPEAVIVssWriterComponents@@@Z` | `0x5DB90` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `?OnBackupShutdown@CVssWriter@@UEAA_NU_GUID@@@Z` | `0x5DB90` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `?OnContinueIOOnVolume@CVssWriter@@UEAA_NPEAGU_GUID@@1@Z` | `0x5DB90` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `?OnIdentify@CVssWriter@@UEAA_NPEAVIVssCreateWriterMetadata@@@Z` | `0x5DB90` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `?OnPostRestore@CVssWriter@@UEAA_NPEAVIVssWriterComponents@@@Z` | `0x5DB90` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `?OnPostSnapshot@CVssWriter@@UEAA_NPEAVIVssWriterComponents@@@Z` | `0x5DB90` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `?OnPreRestore@CVssWriter@@UEAA_NPEAVIVssWriterComponents@@@Z` | `0x5DB90` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `?OnPrepareBackup@CVssWriter@@UEAA_NPEAVIVssWriterComponents@@@Z` | `0x5DB90` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `?OnVSSApplicationStartup@CVssWriter@@UEAA_NXZ` | `0x5DB90` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `?OnVSSShutdown@CVssWriter@@UEAA_NXZ` | `0x5DB90` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `?SetWriterFailure@CVssWriter@@IEAAJJ@Z` | `0x5E3F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `?Subscribe@CVssWriter@@QEAAJK@Z` | `0x5E420` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `?Unsubscribe@CVssWriter@@QEAAJXZ` | `0x5E720` | 1,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `CreateVssExpressWriterInternal` | `0x5ECE0` | 791 | UnwindData |  |
| 78 | `CreateVssSnapshotSetDescription` | `0x5F000` | 1,166 | UnwindData |  |
| 86 | `LoadVssSnapshotSetDescription` | `0x5F4A0` | 462 | UnwindData |  |
| 8 | `??0CVssJetWriter@@QEAA@XZ` | `0x5F680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??1CVssJetWriter@@UEAA@XZ` | `0x5F6A0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `?AreComponentsSelected@CVssJetWriter@@IEBA_NXZ` | `0x5F740` | 196 | UnwindData |  |
| 16 | `?GetBackupType@CVssJetWriter@@IEBA?AW4_VSS_BACKUP_TYPE@@XZ` | `0x5F810` | 178 | UnwindData |  |
| 18 | `?GetContext@CVssJetWriter@@IEBAJXZ` | `0x5F8D0` | 194 | UnwindData |  |
| 20 | `?GetCurrentLevel@CVssJetWriter@@IEBA?AW4_VSS_APPLICATION_LEVEL@@XZ` | `0x5F9A0` | 197 | UnwindData |  |
| 22 | `?GetCurrentSnapshotSetId@CVssJetWriter@@IEBA?AU_GUID@@XZ` | `0x5FA70` | 203 | UnwindData |  |
| 24 | `?GetCurrentVolumeArray@CVssJetWriter@@IEBAPEAPEBGXZ` | `0x5FB50` | 196 | UnwindData |  |
| 26 | `?GetCurrentVolumeCount@CVssJetWriter@@IEBAIXZ` | `0x5FC20` | 194 | UnwindData |  |
| 28 | `?GetRestoreType@CVssJetWriter@@IEBA?AW4_VSS_RESTORE_TYPE@@XZ` | `0x5FCF0` | 178 | UnwindData |  |
| 30 | `?GetSnapshotDeviceName@CVssJetWriter@@IEBAJPEBGPEAPEBG@Z` | `0x5FDB0` | 217 | UnwindData |  |
| 32 | `?Initialize@CVssJetWriter@@QEAAJU_GUID@@PEBG_N211K@Z` | `0x5FE90` | 598 | UnwindData |  |
| 35 | `?IsBootableSystemStateBackedUp@CVssJetWriter@@IEBA_NXZ` | `0x603B0` | 196 | UnwindData |  |
| 37 | `?IsPartialFileSupportEnabled@CVssJetWriter@@IEBA_NXZ` | `0x60480` | 180 | UnwindData |  |
| 39 | `?IsPathAffected@CVssJetWriter@@IEBA_NPEBG@Z` | `0x60540` | 210 | UnwindData |  |
| 41 | `?OnAbortBegin@CVssJetWriter@@UEAAXXZ` | `0x60620` | 133 | UnwindData |  |
| 42 | `?OnAbortEnd@CVssJetWriter@@UEAAXXZ` | `0x606B0` | 133 | UnwindData |  |
| 45 | `?OnBackupCompleteBegin@CVssJetWriter@@UEAA_NPEAVIVssWriterComponents@@@Z` | `0x60740` | 135 | UnwindData |  |
| 46 | `?OnBackupCompleteEnd@CVssJetWriter@@UEAA_NPEAVIVssWriterComponents@@_N@Z` | `0x607D0` | 135 | UnwindData |  |
| 49 | `?OnFreezeBegin@CVssJetWriter@@UEAA_NXZ` | `0x60860` | 135 | UnwindData |  |
| 50 | `?OnFreezeEnd@CVssJetWriter@@UEAA_N_N@Z` | `0x608F0` | 149 | UnwindData |  |
| 51 | `?OnIdentify@CVssJetWriter@@UEAA_NPEAVIVssCreateWriterMetadata@@@Z` | `0x60990` | 135 | UnwindData |  |
| 54 | `?OnPostRestoreBegin@CVssJetWriter@@UEAA_NPEAVIVssWriterComponents@@@Z` | `0x60A20` | 135 | UnwindData |  |
| 55 | `?OnPostRestoreEnd@CVssJetWriter@@UEAA_NPEAVIVssWriterComponents@@_N@Z` | `0x60AB0` | 135 | UnwindData |  |
| 56 | `?OnPostSnapshot@CVssJetWriter@@UEAA_NPEAVIVssWriterComponents@@@Z` | `0x60B40` | 135 | UnwindData |  |
| 59 | `?OnPreRestoreBegin@CVssJetWriter@@UEAA_NPEAVIVssWriterComponents@@@Z` | `0x60BD0` | 135 | UnwindData |  |
| 60 | `?OnPreRestoreEnd@CVssJetWriter@@UEAA_NPEAVIVssWriterComponents@@_N@Z` | `0x60C60` | 135 | UnwindData |  |
| 62 | `?OnPrepareBackupBegin@CVssJetWriter@@UEAA_NPEAVIVssWriterComponents@@@Z` | `0x60CF0` | 135 | UnwindData |  |
| 63 | `?OnPrepareBackupEnd@CVssJetWriter@@UEAA_NPEAVIVssWriterComponents@@_N@Z` | `0x60D80` | 150 | UnwindData |  |
| 64 | `?OnPrepareSnapshotBegin@CVssJetWriter@@UEAA_NXZ` | `0x60E20` | 135 | UnwindData |  |
| 65 | `?OnPrepareSnapshotEnd@CVssJetWriter@@UEAA_N_N@Z` | `0x60EB0` | 149 | UnwindData |  |
| 66 | `?OnThawBegin@CVssJetWriter@@UEAA_NXZ` | `0x60F50` | 135 | UnwindData |  |
| 67 | `?OnThawEnd@CVssJetWriter@@UEAA_N_N@Z` | `0x60FE0` | 149 | UnwindData |  |
| 70 | `?SetWriterFailure@CVssJetWriter@@IEAAJJ@Z` | `0x61080` | 214 | UnwindData |  |
| 73 | `?Uninitialize@CVssJetWriter@@QEAAXXZ` | `0x61160` | 35 | UnwindData |  |
