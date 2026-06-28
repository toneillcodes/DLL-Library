# Binary Specification: authz.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\authz.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `09a59a5dd16a6b50d7f40c121bc207a10bb05a116292036dbf3ea74a1a61ab81`
* **Total Exported Functions:** 68

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `AuthzFreeContext` | `0x1850` | 21 | UnwindData |  |
| 16 | `AuthzInitializeContextFromToken` | `0x45C0` | 185 | UnwindData |  |
| 15 | `AuthzInitializeContextFromSid` | `0x5EC0` | 71 | UnwindData |  |
| 1 | `AuthzAccessCheck` | `0xB660` | 204 | UnwindData |  |
| 11 | `AuthzFreeResourceManager` | `0x11210` | 94 | UnwindData |  |
| 42 | `AuthziFreeAuditQueue` | `0x113B0` | 242 | UnwindData |  |
| 51 | `AuthziLogAuditEvent` | `0x11CA0` | 524 | UnwindData |  |
| 7 | `AuthzFreeAuditEvent` | `0x12330` | 83 | UnwindData |  |
| 58 | `AuthziSourceAudit` | `0x12800` | 373 | UnwindData |  |
| 38 | `AuthziAllocateAuditParams` | `0x12980` | 144 | UnwindData |  |
| 41 | `AuthziFreeAuditParams` | `0x12A20` | 105 | UnwindData |  |
| 40 | `AuthziFreeAuditEventType` | `0x12A90` | 43 | UnwindData |  |
| 45 | `AuthziInitializeAuditEventType` | `0x12AD0` | 286 | UnwindData |  |
| 48 | `AuthziInitializeAuditParamsWithRM` | `0x12CE0` | 423 | UnwindData |  |
| 46 | `AuthziInitializeAuditParams` | `0x12E90` | 98 | UnwindData |  |
| 21 | `AuthzInitializeResourceManager` | `0x13430` | 224 | UnwindData |  |
| 47 | `AuthziInitializeAuditParamsFromArray` | `0x138A0` | 477 | UnwindData |  |
| 44 | `AuthziInitializeAuditEvent` | `0x13C60` | 740 | UnwindData |  |
| 49 | `AuthziInitializeAuditQueue` | `0x13F50` | 498 | UnwindData |  |
| 31 | `AuthzReportSecurityEventFromParams` | `0x14150` | 380 | UnwindData |  |
| 18 | `AuthzInitializeObjectAccessAuditEvent2` | `0x144C0` | 166 | UnwindData |  |
| 12 | `AuthzGetInformationFromContext` | `0x148A0` | 129 | UnwindData |  |
| 37 | `AuthziAccessCheckEx` | `0x17240` | 139 | UnwindData |  |
| 56 | `AuthziModifySecurityAttributes` | `0x172E0` | 96 | UnwindData |  |
| 23 | `AuthzInstallSecurityEventSource` | `0x17700` | 1,049 | UnwindData |  |
| 36 | `AuthzUnregisterSecurityEventSource` | `0x18500` | 155 | UnwindData |  |
| 67 | `InitializeClaimDictionary` | `0x185B0` | 391 | UnwindData |  |
| 29 | `AuthzRegisterSecurityEventSource` | `0x18740` | 201 | UnwindData |  |
| 59 | `FreeClaimDefinitions` | `0x18810` | 167 | UnwindData |  |
| 14 | `AuthzInitializeContextFromAuthzContext` | `0x188C0` | 218 | UnwindData |  |
| 43 | `AuthziGenerateAdminAlertAuditW` | `0x1B070` | 563 | UnwindData |  |
| 2 | `AuthzAddSidsToContext` | `0x1B690` | 268 | UnwindData |  |
| 3 | `AuthzCachedAccessCheck` | `0x1B7B0` | 1,407 | UnwindData |  |
| 5 | `AuthzEnumerateSecurityEventSources` | `0x1BD40` | 1,545 | UnwindData |  |
| 6 | `AuthzEvaluateSacl` | `0x1C350` | 135 | UnwindData |  |
| 8 | `AuthzFreeCentralAccessPolicyCache` | `0x1C3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `AuthzFreeHandle` | `0x1C3F0` | 139 | UnwindData |  |
| 13 | `AuthzInitializeCompoundContext` | `0x1C490` | 276 | UnwindData |  |
| 17 | `AuthzInitializeObjectAccessAuditEvent` | `0x1C5B0` | 70 | UnwindData |  |
| 19 | `AuthzInitializeRemoteAccessCheck` | `0x1C600` | 56 | UnwindData |  |
| 20 | `AuthzInitializeRemoteResourceManager` | `0x1C640` | 56 | UnwindData |  |
| 22 | `AuthzInitializeResourceManagerEx` | `0x1C680` | 160 | UnwindData |  |
| 24 | `AuthzModifyClaims` | `0x1C730` | 109 | UnwindData |  |
| 25 | `AuthzModifySecurityAttributes` | `0x1C7B0` | 96 | UnwindData |  |
| 26 | `AuthzModifySids` | `0x1C820` | 111 | UnwindData |  |
| 27 | `AuthzOpenObjectAudit` | `0x1C8A0` | 519 | UnwindData |  |
| 28 | `AuthzRegisterCapChangeNotification` | `0x1CAB0` | 232 | UnwindData |  |
| 30 | `AuthzReportSecurityEvent` | `0x1CBA0` | 186 | UnwindData |  |
| 32 | `AuthzSetAppContainerInformation` | `0x1CC60` | 70 | UnwindData |  |
| 33 | `AuthzShutdownRemoteAccessCheck` | `0x1CCB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `AuthzUninstallSecurityEventSource` | `0x1CCC0` | 160 | UnwindData |  |
| 35 | `AuthzUnregisterCapChangeNotification` | `0x1CD70` | 104 | UnwindData |  |
| 39 | `AuthziCheckContextMembership` | `0x1CDE0` | 86 | UnwindData |  |
| 50 | `AuthziInitializeContextFromSid` | `0x1CE40` | 254 | UnwindData |  |
| 52 | `AuthziModifyAuditEvent` | `0x1CF50` | 53 | UnwindData |  |
| 53 | `AuthziModifyAuditEvent2` | `0x1CF90` | 139 | UnwindData |  |
| 54 | `AuthziModifyAuditEventType` | `0x1D030` | 88 | UnwindData |  |
| 55 | `AuthziModifyAuditQueue` | `0x1D090` | 105 | UnwindData |  |
| 57 | `AuthziQuerySecurityAttributes` | `0x1D100` | 109 | UnwindData |  |
| 61 | `GenerateNewCAPID` | `0x216C0` | 299 | UnwindData |  |
| 66 | `GetDefaultCAPESecurityDescriptor` | `0x21800` | 172 | UnwindData |  |
| 62 | `GetCentralAccessPoliciesByCapID` | `0x269E0` | 611 | UnwindData |  |
| 63 | `GetCentralAccessPoliciesByDN` | `0x26C50` | 613 | UnwindData |  |
| 60 | `FreeClaimDictionary` | `0x27730` | 20 | UnwindData |  |
| 64 | `GetClaimDefinitions` | `0x27750` | 212 | UnwindData |  |
| 65 | `GetClaimDomainInfo` | `0x27830` | 192 | UnwindData |  |
| 68 | `RefreshClaimDictionary` | `0x27900` | 172 | UnwindData |  |
| 4 | `AuthzComputeEffectivePermission` | `0x27FC0` | 435 | UnwindData |  |
