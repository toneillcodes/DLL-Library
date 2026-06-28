# Binary Specification: dmenrollengine.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dmenrollengine.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bcf1c11d851707f4501f23a3f1a828082bc39e4666eb757fb0a7c4839b2ebebd`
* **Total Exported Functions:** 68

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 47 | `GetEnrollmentType` | `0x7D10` | 1,122 | UnwindData |  |
| 45 | `GetEnrollmentState` | `0x8180` | 195 | UnwindData |  |
| 49 | `GetFirstEnrollmentGuidOfTypes` | `0x11200` | 351 | UnwindData |  |
| 26 | `EnrollEngineInitialize` | `0x11A80` | 136 | UnwindData |  |
| 10 | `GetDatabaseManagerInstance` | `0x14530` | 1,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `GetEnrollmentCertStore` | `0x14C60` | 124 | UnwindData |  |
| 56 | `IsLockedToMmpc` | `0x16100` | 1,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `GetMmpcEnrollmentFlag` | `0x165A0` | 66,800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `AutoEnrollMDM` | `0x26A90` | 821 | UnwindData |  |
| 22 | `BeginEnrollmentScope` | `0x26DD0` | 176 | UnwindData |  |
| 68 | `SysprepGeneralize` | `0x270C0` | 204 | UnwindData |  |
| 20 | `VerifyServerIsMmpcEx` | `0x271A0` | 8,800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `DllCanUnloadNow` | `0x29400` | 32 | UnwindData |  |
| 24 | `DllGetActivationFactory` | `0x29430` | 45 | UnwindData |  |
| 25 | `DllGetClassObject` | `0x29470` | 65 | UnwindData |  |
| 29 | `GetEnrollmentAadResourceUrl` | `0x2E4F0` | 29 | UnwindData |  |
| 30 | `GetEnrollmentAadSendDeviceToken` | `0x2E520` | 29 | UnwindData |  |
| 31 | `GetEnrollmentAltitude` | `0x2E550` | 29 | UnwindData |  |
| 32 | `GetEnrollmentAuthPolicy` | `0x2E580` | 29 | UnwindData |  |
| 34 | `GetEnrollmentClientCertThumbprint` | `0x2E5B0` | 39 | UnwindData |  |
| 35 | `GetEnrollmentCurCryptoProvider` | `0x2E5E0` | 39 | UnwindData |  |
| 36 | `GetEnrollmentDiscoveryService` | `0x2E610` | 39 | UnwindData |  |
| 37 | `GetEnrollmentEntDmId` | `0x2E640` | 29 | UnwindData |  |
| 38 | `GetEnrollmentForceAadToken` | `0x2E670` | 29 | UnwindData |  |
| 39 | `GetEnrollmentLinkedEnrollmentHasPriority` | `0x2E6A0` | 29 | UnwindData |  |
| 40 | `GetEnrollmentLinkedEnrollmentId` | `0x2E6D0` | 29 | UnwindData |  |
| 41 | `GetEnrollmentLinkedEnrollmentLockedToMMPC` | `0x2E700` | 29 | UnwindData |  |
| 42 | `GetEnrollmentPartnerOpaqueID` | `0x2E730` | 39 | UnwindData |  |
| 43 | `GetEnrollmentResourceCache` | `0x2E760` | 39 | UnwindData |  |
| 44 | `GetEnrollmentSID` | `0x2E790` | 39 | UnwindData |  |
| 46 | `GetEnrollmentTenantID` | `0x2E7C0` | 39 | UnwindData |  |
| 48 | `GetEnrollmentUPN` | `0x2E7F0` | 39 | UnwindData |  |
| 18 | `GetEnrollmentsOfTypes` | `0x2E820` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `GetIsRecoveryAllowed` | `0x2E850` | 29 | UnwindData |  |
| 11 | `GetProviderID` | `0x2E880` | 39 | UnwindData |  |
| 52 | `GetRecoveryInitiatedByServer` | `0x2E8B0` | 29 | UnwindData |  |
| 53 | `GetRecoveryRetryCount` | `0x2E8E0` | 29 | UnwindData |  |
| 54 | `GetRecoveryStatusEnum` | `0x2E910` | 29 | UnwindData |  |
| 55 | `GetWasPrivateKeyBrokenByRenew` | `0x2E940` | 29 | UnwindData |  |
| 9 | `OpenEnrollmentsHKEY` | `0x2E970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `SetEnrollState` | `0x2E980` | 29 | UnwindData |  |
| 8 | `SetEnrollmentAadResourceUrl` | `0x2E9B0` | 118 | UnwindData |  |
| 17 | `SetEnrollmentAadSendDeviceToken` | `0x2EA30` | 29 | UnwindData |  |
| 15 | `SetEnrollmentDormant` | `0x2EA60` | 111 | UnwindData |  |
| 59 | `SetEnrollmentForceAadToken` | `0x2EAE0` | 29 | UnwindData |  |
| 60 | `SetEnrollmentPartnerOpaqueID` | `0x2EB10` | 29 | UnwindData |  |
| 61 | `SetEnrollmentResourceCache` | `0x2EB40` | 29 | UnwindData |  |
| 13 | `SetEnrollmentUPN` | `0x2EB70` | 118 | UnwindData |  |
| 62 | `SetIsRecoveryAllowed` | `0x2EBF0` | 29 | UnwindData |  |
| 63 | `SetMmpcEnrollmentFlag` | `0x2EC20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `SetProviderID` | `0x2EC30` | 29 | UnwindData |  |
| 64 | `SetRecoveryInitiatedByServer` | `0x2EC60` | 29 | UnwindData |  |
| 65 | `SetRecoveryRetryCount` | `0x2EC90` | 29 | UnwindData |  |
| 66 | `SetRecoveryStateAndErrorCode` | `0x2ECC0` | 29 | UnwindData |  |
| 67 | `SetWasPrivateKeyBrokenByRenew` | `0x2ECF0` | 29 | UnwindData |  |
| 14 | `SwitchAADLinkedEnrollment` | `0x2ED20` | 177 | UnwindData |  |
| 16 | `_IsManagementRegistrationAllowed` | `0x2F0F0` | 54,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `GetEnrollmentClientContext` | `0x3C460` | 346 | UnwindData |  |
| 28 | `GetCertificatePolicy` | `0x3DBF0` | 241 | UnwindData |  |
| 3 | `CleanupExpiredOMADMSessions` | `0x3E3B0` | 534 | UnwindData |  |
| 4 | `EnableLogging` | `0x47DC0` | 123,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `FindDiscoveryService` | `0x65FC0` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DiscoverEndpoint` | `0x662D0` | 203 | UnwindData |  |
| 5 | `DiscoverEndpointEx` | `0x663B0` | 236 | UnwindData |  |
| 19 | `DiscoverEndpointEx2` | `0x664B0` | 713 | UnwindData |  |
| 6 | `FindDiscoveryServiceEx` | `0x66780` | 665 | UnwindData |  |
| 27 | `FreeMmpcDiscoveryResultsData` | `0x66C60` | 74 | UnwindData |  |
| 57 | `MmpcDiscoverEndpoint` | `0x66CB0` | 448 | UnwindData |  |
