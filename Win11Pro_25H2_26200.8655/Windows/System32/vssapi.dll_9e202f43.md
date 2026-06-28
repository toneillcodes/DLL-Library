# Binary Specification: vssapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\vssapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9e202f43c6191b45239a6d8d001f1e62753fc9a56039e5581a6dfd93e6f0ca4e`
* **Total Exported Functions:** 84

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 15 | `?CreateVssExamineWriterMetadata@@YAJPEAGPEAPEAVIVssExamineWriterMetadata@@@Z` | `0x1E9B0` | 1,029 | UnwindData |  |
| 76 | `CreateVssExamineWriterMetadataInternal` | `0x1E9B0` | 1,029 | UnwindData |  |
| 79 | `CreateWriter` | `0x3E530` | 228 | UnwindData |  |
| 6 | `VssFreeSnapshotProperties` | `0x43710` | 291 | UnwindData |  |
| 88 | `VssFreeSnapshotPropertiesInternal` | `0x43710` | 291 | UnwindData |  |
| 14 | `?CreateVssBackupComponents@@YAJPEAPEAVIVssBackupComponents@@@Z` | `0x49830` | 487 | UnwindData |  |
| 75 | `CreateVssBackupComponentsInternal` | `0x49830` | 487 | UnwindData |  |
| 81 | `DllCanUnloadNow` | `0x4AAF0` | 20,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `CreateWriterEx` | `0x4FCB0` | 236 | UnwindData |  |
| 82 | `DllGetClassObject` | `0x59040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `GetProviderMgmtInterface` | `0x59060` | 1,077 | UnwindData |  |
| 84 | `GetProviderMgmtInterfaceInternal` | `0x59060` | 1,077 | UnwindData |  |
| 5 | `IsVolumeSnapshotted` | `0x594A0` | 3,046 | UnwindData |  |
| 85 | `IsVolumeSnapshottedInternal` | `0x594A0` | 3,046 | UnwindData |  |
| 7 | `ShouldBlockRevert` | `0x5A090` | 3,664 | UnwindData |  |
| 87 | `ShouldBlockRevertInternal` | `0x5A090` | 3,664 | UnwindData |  |
| 9 | `??0CVssWriter@@QEAA@XZ` | `0x5B550` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??1CVssWriter@@UEAA@XZ` | `0x5B850` | 1,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `?AreComponentsSelected@CVssWriter@@IEBA_NXZ` | `0x5BC60` | 33 | UnwindData |  |
| 17 | `?GetBackupType@CVssWriter@@IEBA?AW4_VSS_BACKUP_TYPE@@XZ` | `0x5C0D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `?GetContext@CVssWriter@@IEBAJXZ` | `0x5C0E0` | 33 | UnwindData |  |
| 21 | `?GetCurrentLevel@CVssWriter@@IEBA?AW4_VSS_APPLICATION_LEVEL@@XZ` | `0x5C260` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `?GetCurrentSnapshotSetId@CVssWriter@@IEBA?AU_GUID@@XZ` | `0x5C300` | 24 | UnwindData |  |
| 25 | `?GetCurrentVolumeArray@CVssWriter@@IEBAPEAPEBGXZ` | `0x5C320` | 33 | UnwindData |  |
| 27 | `?GetCurrentVolumeCount@CVssWriter@@IEBAIXZ` | `0x5C350` | 33 | UnwindData |  |
| 29 | `?GetRestoreType@CVssWriter@@IEBA?AW4_VSS_RESTORE_TYPE@@XZ` | `0x5C950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `?GetSnapshotDeviceName@CVssWriter@@IEBAJPEBGPEAPEBG@Z` | `0x5C960` | 2,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `?Initialize@CVssWriter@@QEAAJU_GUID@@PEBGW4VSS_USAGE_TYPE@@W4VSS_SOURCE_TYPE@@W4_VSS_APPLICATION_LEVEL@@KW4VSS_ALTERNATE_WRITER_STATE@@_N1@Z` | `0x5D200` | 97 | UnwindData |  |
| 34 | `?InstallAlternateWriter@CVssWriter@@QEAAJU_GUID@@0@Z` | `0x5D270` | 70 | UnwindData |  |
| 36 | `?IsBootableSystemStateBackedUp@CVssWriter@@IEBA_NXZ` | `0x5D350` | 33 | UnwindData |  |
| 38 | `?IsPartialFileSupportEnabled@CVssWriter@@IEBA_NXZ` | `0x5D3A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `?IsPathAffected@CVssWriter@@IEBA_NPEBG@Z` | `0x5D3B0` | 33 | UnwindData |  |
| 43 | `?OnBackOffIOOnVolume@CVssWriter@@UEAA_NPEAGU_GUID@@1@Z` | `0x5DB60` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `?OnBackupComplete@CVssWriter@@UEAA_NPEAVIVssWriterComponents@@@Z` | `0x5DB60` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `?OnBackupShutdown@CVssWriter@@UEAA_NU_GUID@@@Z` | `0x5DB60` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `?OnContinueIOOnVolume@CVssWriter@@UEAA_NPEAGU_GUID@@1@Z` | `0x5DB60` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `?OnIdentify@CVssWriter@@UEAA_NPEAVIVssCreateWriterMetadata@@@Z` | `0x5DB60` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `?OnPostRestore@CVssWriter@@UEAA_NPEAVIVssWriterComponents@@@Z` | `0x5DB60` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `?OnPostSnapshot@CVssWriter@@UEAA_NPEAVIVssWriterComponents@@@Z` | `0x5DB60` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `?OnPreRestore@CVssWriter@@UEAA_NPEAVIVssWriterComponents@@@Z` | `0x5DB60` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `?OnPrepareBackup@CVssWriter@@UEAA_NPEAVIVssWriterComponents@@@Z` | `0x5DB60` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `?OnVSSApplicationStartup@CVssWriter@@UEAA_NXZ` | `0x5DB60` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `?OnVSSShutdown@CVssWriter@@UEAA_NXZ` | `0x5DB60` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `?SetWriterFailure@CVssWriter@@IEAAJJ@Z` | `0x5E3C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `?Subscribe@CVssWriter@@QEAAJK@Z` | `0x5E3F0` | 768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `?Unsubscribe@CVssWriter@@QEAAJXZ` | `0x5E6F0` | 1,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `CreateVssExpressWriterInternal` | `0x5ECB0` | 791 | UnwindData |  |
| 78 | `CreateVssSnapshotSetDescription` | `0x5EFD0` | 1,166 | UnwindData |  |
| 86 | `LoadVssSnapshotSetDescription` | `0x5F470` | 462 | UnwindData |  |
| 8 | `??0CVssJetWriter@@QEAA@XZ` | `0x5F650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??1CVssJetWriter@@UEAA@XZ` | `0x5F670` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `?AreComponentsSelected@CVssJetWriter@@IEBA_NXZ` | `0x5F710` | 196 | UnwindData |  |
| 16 | `?GetBackupType@CVssJetWriter@@IEBA?AW4_VSS_BACKUP_TYPE@@XZ` | `0x5F7E0` | 178 | UnwindData |  |
| 18 | `?GetContext@CVssJetWriter@@IEBAJXZ` | `0x5F8A0` | 194 | UnwindData |  |
| 20 | `?GetCurrentLevel@CVssJetWriter@@IEBA?AW4_VSS_APPLICATION_LEVEL@@XZ` | `0x5F970` | 197 | UnwindData |  |
| 22 | `?GetCurrentSnapshotSetId@CVssJetWriter@@IEBA?AU_GUID@@XZ` | `0x5FA40` | 203 | UnwindData |  |
| 24 | `?GetCurrentVolumeArray@CVssJetWriter@@IEBAPEAPEBGXZ` | `0x5FB20` | 196 | UnwindData |  |
| 26 | `?GetCurrentVolumeCount@CVssJetWriter@@IEBAIXZ` | `0x5FBF0` | 194 | UnwindData |  |
| 28 | `?GetRestoreType@CVssJetWriter@@IEBA?AW4_VSS_RESTORE_TYPE@@XZ` | `0x5FCC0` | 178 | UnwindData |  |
| 30 | `?GetSnapshotDeviceName@CVssJetWriter@@IEBAJPEBGPEAPEBG@Z` | `0x5FD80` | 217 | UnwindData |  |
| 32 | `?Initialize@CVssJetWriter@@QEAAJU_GUID@@PEBG_N211K@Z` | `0x5FE60` | 598 | UnwindData |  |
| 35 | `?IsBootableSystemStateBackedUp@CVssJetWriter@@IEBA_NXZ` | `0x60380` | 196 | UnwindData |  |
| 37 | `?IsPartialFileSupportEnabled@CVssJetWriter@@IEBA_NXZ` | `0x60450` | 180 | UnwindData |  |
| 39 | `?IsPathAffected@CVssJetWriter@@IEBA_NPEBG@Z` | `0x60510` | 210 | UnwindData |  |
| 41 | `?OnAbortBegin@CVssJetWriter@@UEAAXXZ` | `0x605F0` | 133 | UnwindData |  |
| 42 | `?OnAbortEnd@CVssJetWriter@@UEAAXXZ` | `0x60680` | 133 | UnwindData |  |
| 45 | `?OnBackupCompleteBegin@CVssJetWriter@@UEAA_NPEAVIVssWriterComponents@@@Z` | `0x60710` | 135 | UnwindData |  |
| 46 | `?OnBackupCompleteEnd@CVssJetWriter@@UEAA_NPEAVIVssWriterComponents@@_N@Z` | `0x607A0` | 135 | UnwindData |  |
| 49 | `?OnFreezeBegin@CVssJetWriter@@UEAA_NXZ` | `0x60830` | 135 | UnwindData |  |
| 50 | `?OnFreezeEnd@CVssJetWriter@@UEAA_N_N@Z` | `0x608C0` | 149 | UnwindData |  |
| 51 | `?OnIdentify@CVssJetWriter@@UEAA_NPEAVIVssCreateWriterMetadata@@@Z` | `0x60960` | 135 | UnwindData |  |
| 54 | `?OnPostRestoreBegin@CVssJetWriter@@UEAA_NPEAVIVssWriterComponents@@@Z` | `0x609F0` | 135 | UnwindData |  |
| 55 | `?OnPostRestoreEnd@CVssJetWriter@@UEAA_NPEAVIVssWriterComponents@@_N@Z` | `0x60A80` | 135 | UnwindData |  |
| 56 | `?OnPostSnapshot@CVssJetWriter@@UEAA_NPEAVIVssWriterComponents@@@Z` | `0x60B10` | 135 | UnwindData |  |
| 59 | `?OnPreRestoreBegin@CVssJetWriter@@UEAA_NPEAVIVssWriterComponents@@@Z` | `0x60BA0` | 135 | UnwindData |  |
| 60 | `?OnPreRestoreEnd@CVssJetWriter@@UEAA_NPEAVIVssWriterComponents@@_N@Z` | `0x60C30` | 135 | UnwindData |  |
| 62 | `?OnPrepareBackupBegin@CVssJetWriter@@UEAA_NPEAVIVssWriterComponents@@@Z` | `0x60CC0` | 135 | UnwindData |  |
| 63 | `?OnPrepareBackupEnd@CVssJetWriter@@UEAA_NPEAVIVssWriterComponents@@_N@Z` | `0x60D50` | 150 | UnwindData |  |
| 64 | `?OnPrepareSnapshotBegin@CVssJetWriter@@UEAA_NXZ` | `0x60DF0` | 135 | UnwindData |  |
| 65 | `?OnPrepareSnapshotEnd@CVssJetWriter@@UEAA_N_N@Z` | `0x60E80` | 149 | UnwindData |  |
| 66 | `?OnThawBegin@CVssJetWriter@@UEAA_NXZ` | `0x60F20` | 135 | UnwindData |  |
| 67 | `?OnThawEnd@CVssJetWriter@@UEAA_N_N@Z` | `0x60FB0` | 149 | UnwindData |  |
| 70 | `?SetWriterFailure@CVssJetWriter@@IEAAJJ@Z` | `0x61050` | 214 | UnwindData |  |
| 73 | `?Uninitialize@CVssJetWriter@@QEAAXXZ` | `0x61130` | 35 | UnwindData |  |
