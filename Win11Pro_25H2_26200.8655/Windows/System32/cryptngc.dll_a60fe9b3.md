# Binary Specification: cryptngc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\cryptngc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a60fe9b3ca358549d0b6798b642ae8919d91c9cf541305010dc943d7b51b20c0`
* **Total Exported Functions:** 59

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 18 | `NgcDecryptWithUserIdKeySilent` | `0x2830` | 50 | UnwindData |  |
| 48 | `NgcQueryEnabled` | `0x74A0` | 1,009 | UnwindData |  |
| 45 | `NgcPackAuthBuffer` | `0x9310` | 1,260 | UnwindData |  |
| 31 | `NgcGetKeyImplType` | `0x9810` | 776 | UnwindData |  |
| 58 | `NgcUnpackCredData` | `0x12F40` | 148 | UnwindData |  |
| 25 | `NgcFreeEnumState` | `0x17EF0` | 184 | UnwindData |  |
| 24 | `NgcEnumUserIdKeys` | `0x17FF0` | 500 | UnwindData |  |
| 40 | `NgcGetUserIdKeyPublicKey` | `0x19120` | 365 | UnwindData |  |
| 37 | `NgcGetUserIdKeyCertificate` | `0x192A0` | 298 | UnwindData |  |
| 26 | `NgcGetDefaultDecryptionKeyName` | `0x19620` | 353 | UnwindData |  |
| 16 | `NgcCreateUserIdKeyHandle` | `0x197F0` | 436 | UnwindData |  |
| 44 | `NgcOpenUserIdKey` | `0x1B250` | 85 | UnwindData |  |
| 47 | `NgcQueryEffectiveCertPolicy` | `0x1C310` | 58 | UnwindData |  |
| 49 | `NgcQueryHardwarePolicy` | `0x1CA30` | 59 | UnwindData |  |
| 27 | `NgcGetEventInterface` | `0x1D1A0` | 3,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `NgcEnumContainers` | `0x1DF40` | 71 | UnwindData |  |
| 39 | `NgcGetUserIdKeyName` | `0x28A70` | 97 | UnwindData |  |
| 41 | `NgcIsAnyContainerInVsm` | `0x29640` | 95 | UnwindData |  |
| 1 | `FidoCreateCredential` | `0x2F360` | 4,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `FidoGetCredential` | `0x2F360` | 4,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `FidoSignWithCredential` | `0x2F360` | 4,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `NgcGetKeyAttestationForContainerService` | `0x30300` | 662 | UnwindData |  |
| 29 | `NgcGetKeyAttestationForUserIdKey` | `0x305A0` | 73 | UnwindData |  |
| 30 | `NgcGetKeyAttestationForUserIdKey2` | `0x305F0` | 649 | UnwindData |  |
| 46 | `NgcPackPasswordChangeAuthBuffer` | `0x31940` | 156 | UnwindData |  |
| 57 | `NgcUnpackAuthBuffer` | `0x319F0` | 206 | UnwindData |  |
| 59 | `NgcUnpackPasswordChangeAuthBuffer` | `0x31AD0` | 206 | UnwindData |  |
| 43 | `NgcNotifyVscProvisioned` | `0x31C90` | 280 | UnwindData |  |
| 4 | `NgcAddBioProtector` | `0x338D0` | 360 | UnwindData |  |
| 5 | `NgcAddCompanionDeviceProtector` | `0x33A40` | 348 | UnwindData |  |
| 6 | `NgcAddPrebootProtector` | `0x33BB0` | 381 | UnwindData |  |
| 7 | `NgcCancelPendingUIRequest` | `0x33D40` | 318 | UnwindData |  |
| 8 | `NgcChangePin` | `0x33E90` | 348 | UnwindData |  |
| 9 | `NgcChangePinSilent` | `0x34000` | 368 | UnwindData |  |
| 10 | `NgcCreateContainer` | `0x34180` | 1,081 | UnwindData |  |
| 11 | `NgcCreateContainerSilent` | `0x345C0` | 496 | UnwindData |  |
| 19 | `NgcDeleteContainer` | `0x347C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `NgcDeleteContainerEx` | `0x347D0` | 925 | UnwindData |  |
| 34 | `NgcGetPolicy` | `0x34B80` | 368 | UnwindData |  |
| 42 | `NgcIsPinRemovable` | `0x34D00` | 660 | UnwindData |  |
| 50 | `NgcRemoveBioProtector` | `0x34FA0` | 336 | UnwindData |  |
| 51 | `NgcRemoveCompanionDeviceProtector` | `0x35100` | 336 | UnwindData |  |
| 52 | `NgcRemovePrebootProtector` | `0x35260` | 336 | UnwindData |  |
| 14 | `NgcCreateUserIdKey` | `0x380E0` | 481 | UnwindData |  |
| 15 | `NgcCreateUserIdKeyEx` | `0x382D0` | 498 | UnwindData |  |
| 21 | `NgcDeleteUserIdKey` | `0x384D0` | 286 | UnwindData |  |
| 32 | `NgcGetLogonDecryptionKeyName` | `0x38600` | 298 | UnwindData |  |
| 33 | `NgcGetLogonDecryptionKeyNameForFirstLogonAfterUpgradeFromThreshold` | `0x38730` | 298 | UnwindData |  |
| 35 | `NgcGetPregenKeyState` | `0x38860` | 267 | UnwindData |  |
| 36 | `NgcGetPregenUserKey` | `0x38980` | 349 | UnwindData |  |
| 38 | `NgcGetUserIdKeyContainerStatus` | `0x38AF0` | 320 | UnwindData |  |
| 53 | `NgcSignWithUserIdKey` | `0x38C40` | 68 | UnwindData |  |
| 54 | `NgcSignWithUserIdKeyAndPadding` | `0x38C90` | 165 | UnwindData |  |
| 55 | `NgcSignWithUserIdKeyEx` | `0x38D40` | 151 | UnwindData |  |
| 56 | `NgcSignWithUserIdKeySilent` | `0x38DE0` | 87 | UnwindData |  |
| 17 | `NgcDecryptWithUserIdKey` | `0x395F0` | 52 | UnwindData |  |
| 22 | `NgcEncryptWithAsymmetricKey` | `0x39630` | 327 | UnwindData |  |
| 12 | `NgcCreateTicketForSmartCardKeyOperation` | `0x39780` | 117 | UnwindData |  |
| 13 | `NgcCreateTicketForSmartCardVpn` | `0x39800` | 59,404 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
