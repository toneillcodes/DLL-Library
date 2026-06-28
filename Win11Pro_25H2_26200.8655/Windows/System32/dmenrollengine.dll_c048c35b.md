# Binary Specification: dmenrollengine.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dmenrollengine.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c048c35bb9c58e21eeb74d2b4b8b6097d4eb8d1ea9aab2e7d303d9552936a678`
* **Total Exported Functions:** 68

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 47 | `GetEnrollmentType` | `0x7D20` | 1,122 | UnwindData |  |
| 45 | `GetEnrollmentState` | `0x8190` | 195 | UnwindData |  |
| 49 | `GetFirstEnrollmentGuidOfTypes` | `0x11210` | 351 | UnwindData |  |
| 26 | `EnrollEngineInitialize` | `0x11A90` | 136 | UnwindData |  |
| 10 | `GetDatabaseManagerInstance` | `0x14540` | 1,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `GetEnrollmentCertStore` | `0x14B70` | 124 | UnwindData |  |
| 56 | `IsLockedToMmpc` | `0x16010` | 1,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `GetMmpcEnrollmentFlag` | `0x16590` | 73,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `AutoEnrollMDM` | `0x282F0` | 821 | UnwindData |  |
| 22 | `BeginEnrollmentScope` | `0x28630` | 176 | UnwindData |  |
| 68 | `SysprepGeneralize` | `0x28920` | 204 | UnwindData |  |
| 20 | `VerifyServerIsMmpcEx` | `0x28A00` | 8,800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `DllCanUnloadNow` | `0x2AC60` | 32 | UnwindData |  |
| 24 | `DllGetActivationFactory` | `0x2AC90` | 45 | UnwindData |  |
| 25 | `DllGetClassObject` | `0x2ACD0` | 65 | UnwindData |  |
| 29 | `GetEnrollmentAadResourceUrl` | `0x2FD20` | 29 | UnwindData |  |
| 30 | `GetEnrollmentAadSendDeviceToken` | `0x2FD50` | 29 | UnwindData |  |
| 31 | `GetEnrollmentAltitude` | `0x2FD80` | 29 | UnwindData |  |
| 32 | `GetEnrollmentAuthPolicy` | `0x2FDB0` | 29 | UnwindData |  |
| 34 | `GetEnrollmentClientCertThumbprint` | `0x2FDE0` | 39 | UnwindData |  |
| 35 | `GetEnrollmentCurCryptoProvider` | `0x2FE10` | 39 | UnwindData |  |
| 36 | `GetEnrollmentDiscoveryService` | `0x2FE40` | 39 | UnwindData |  |
| 37 | `GetEnrollmentEntDmId` | `0x2FE70` | 29 | UnwindData |  |
| 38 | `GetEnrollmentForceAadToken` | `0x2FEA0` | 29 | UnwindData |  |
| 39 | `GetEnrollmentLinkedEnrollmentHasPriority` | `0x2FED0` | 29 | UnwindData |  |
| 40 | `GetEnrollmentLinkedEnrollmentId` | `0x2FF00` | 29 | UnwindData |  |
| 41 | `GetEnrollmentLinkedEnrollmentLockedToMMPC` | `0x2FF30` | 29 | UnwindData |  |
| 42 | `GetEnrollmentPartnerOpaqueID` | `0x2FF60` | 39 | UnwindData |  |
| 43 | `GetEnrollmentResourceCache` | `0x2FF90` | 39 | UnwindData |  |
| 44 | `GetEnrollmentSID` | `0x2FFC0` | 39 | UnwindData |  |
| 46 | `GetEnrollmentTenantID` | `0x2FFF0` | 39 | UnwindData |  |
| 48 | `GetEnrollmentUPN` | `0x30020` | 39 | UnwindData |  |
| 18 | `GetEnrollmentsOfTypes` | `0x30050` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `GetIsRecoveryAllowed` | `0x30080` | 29 | UnwindData |  |
| 11 | `GetProviderID` | `0x300B0` | 39 | UnwindData |  |
| 52 | `GetRecoveryInitiatedByServer` | `0x300E0` | 29 | UnwindData |  |
| 53 | `GetRecoveryRetryCount` | `0x30110` | 29 | UnwindData |  |
| 54 | `GetRecoveryStatusEnum` | `0x30140` | 29 | UnwindData |  |
| 55 | `GetWasPrivateKeyBrokenByRenew` | `0x30170` | 29 | UnwindData |  |
| 9 | `OpenEnrollmentsHKEY` | `0x301A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `SetEnrollState` | `0x301B0` | 29 | UnwindData |  |
| 8 | `SetEnrollmentAadResourceUrl` | `0x301E0` | 118 | UnwindData |  |
| 17 | `SetEnrollmentAadSendDeviceToken` | `0x30260` | 29 | UnwindData |  |
| 15 | `SetEnrollmentDormant` | `0x30290` | 111 | UnwindData |  |
| 59 | `SetEnrollmentForceAadToken` | `0x30310` | 29 | UnwindData |  |
| 60 | `SetEnrollmentPartnerOpaqueID` | `0x30340` | 29 | UnwindData |  |
| 61 | `SetEnrollmentResourceCache` | `0x30370` | 29 | UnwindData |  |
| 13 | `SetEnrollmentUPN` | `0x303A0` | 118 | UnwindData |  |
| 62 | `SetIsRecoveryAllowed` | `0x30420` | 29 | UnwindData |  |
| 63 | `SetMmpcEnrollmentFlag` | `0x30450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `SetProviderID` | `0x30460` | 29 | UnwindData |  |
| 64 | `SetRecoveryInitiatedByServer` | `0x30490` | 29 | UnwindData |  |
| 65 | `SetRecoveryRetryCount` | `0x304C0` | 29 | UnwindData |  |
| 66 | `SetRecoveryStateAndErrorCode` | `0x304F0` | 29 | UnwindData |  |
| 67 | `SetWasPrivateKeyBrokenByRenew` | `0x30520` | 29 | UnwindData |  |
| 14 | `SwitchAADLinkedEnrollment` | `0x30550` | 177 | UnwindData |  |
| 16 | `_IsManagementRegistrationAllowed` | `0x30920` | 54,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `GetEnrollmentClientContext` | `0x3DC90` | 346 | UnwindData |  |
| 28 | `GetCertificatePolicy` | `0x3EAB0` | 241 | UnwindData |  |
| 3 | `CleanupExpiredOMADMSessions` | `0x3F270` | 534 | UnwindData |  |
| 4 | `EnableLogging` | `0x48C80` | 123,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `FindDiscoveryService` | `0x66DE0` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DiscoverEndpoint` | `0x67110` | 203 | UnwindData |  |
| 5 | `DiscoverEndpointEx` | `0x671F0` | 236 | UnwindData |  |
| 19 | `DiscoverEndpointEx2` | `0x672F0` | 713 | UnwindData |  |
| 6 | `FindDiscoveryServiceEx` | `0x675C0` | 665 | UnwindData |  |
| 27 | `FreeMmpcDiscoveryResultsData` | `0x67AA0` | 74 | UnwindData |  |
| 57 | `MmpcDiscoverEndpoint` | `0x67AF0` | 448 | UnwindData |  |
