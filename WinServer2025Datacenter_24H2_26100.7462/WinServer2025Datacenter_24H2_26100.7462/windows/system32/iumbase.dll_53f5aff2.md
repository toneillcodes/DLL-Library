# Binary Specification: iumbase.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\iumbase.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `53f5aff2efa55263de95a7dd77e9e94407be73e41f4202a4ccc4b2931281a780`
* **Total Exported Functions:** 37

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `AssignMemoryToSocDomain` | `0x12C0` | 107 | UnwindData |  |
| 2 | `AwaitSmc` | `0x1340` | 49 | UnwindData |  |
| 3 | `CreateSecureDevice` | `0x1380` | 60 | UnwindData |  |
| 4 | `CreateSecureSection` | `0x13D0` | 85 | UnwindData |  |
| 5 | `CreateSecureSectionSpecifyPages` | `0x1430` | 96 | UnwindData |  |
| 6 | `DecryptData` | `0x14A0` | 194 | UnwindData |  |
| 7 | `DecryptISKBoundData` | `0x1570` | 168 | UnwindData |  |
| 8 | `DmaMapMemory` | `0x1620` | 157 | UnwindData |  |
| 9 | `EmitSmc` | `0x16D0` | 49 | UnwindData |  |
| 10 | `EncryptData` | `0x1710` | 196 | UnwindData |  |
| 11 | `FlushSecureSectionBuffers` | `0x17E0` | 49 | UnwindData |  |
| 12 | `GetDmaEnabler` | `0x1820` | 103 | UnwindData |  |
| 13 | `GetExposedSecureSection` | `0x1890` | 63 | UnwindData |  |
| 14 | `GetFipsModeFromIumKernelState` | `0x18E0` | 149 | UnwindData |  |
| 15 | `GetSecureIdentityKey` | `0x1980` | 110 | UnwindData |  |
| 16 | `GetSecureIdentitySigningKey` | `0x1A00` | 113 | UnwindData |  |
| 17 | `GetSeedFromIumKernelState` | `0x1A80` | 187 | UnwindData |  |
| 18 | `GetSignedReport` | `0x1B50` | 245 | UnwindData |  |
| 19 | `GetTaggedData` | `0x1C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `GetTaggedDataSize` | `0x1C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `GetTpmBindingInfo` | `0x1C70` | 157 | UnwindData |  |
| 22 | `IsSecureProcess` | `0x1D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `MapSecureIo` | `0x1D40` | 83 | UnwindData |  |
| 24 | `OpenCurrentExtension` | `0x1DA0` | 60 | UnwindData |  |
| 25 | `OpenSecureSection` | `0x1DF0` | 63 | UnwindData |  |
| 26 | `PostMailbox` | `0x1E40` | 63 | UnwindData |  |
| 27 | `ProtectSecureIo` | `0x1E90` | 68 | UnwindData |  |
| 28 | `QuerySecureDeviceInformation` | `0x1EE0` | 87 | UnwindData |  |
| 29 | `SecureProcessUsesAttestedKeys` | `0x1F40` | 25 | UnwindData |  |
| 30 | `SecureStorageGet` | `0x1F60` | 63 | UnwindData |  |
| 31 | `SecureStoragePut` | `0x1FB0` | 63 | UnwindData |  |
| 32 | `SetDmaTargetProperties` | `0x2000` | 87 | UnwindData |  |
| 33 | `SetPolicyExtension` | `0x2060` | 49 | UnwindData |  |
| 34 | `UnmapSecureIo` | `0x20A0` | 49 | UnwindData |  |
| 35 | `UpdateSecureDeviceState` | `0x20E0` | 49 | UnwindData |  |
| 36 | `VbsVmSysCall` | `0x2120` | 151 | UnwindData |  |
| 37 | `VerifyEnclaveAttestationReport` | `0x21C0` | 116 | UnwindData |  |
