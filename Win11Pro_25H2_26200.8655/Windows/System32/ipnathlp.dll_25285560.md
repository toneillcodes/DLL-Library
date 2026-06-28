# Binary Specification: ipnathlp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ipnathlp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `252855600d22f2ab92c19a42ebceced9c817778a62b46a8579829b9f0ebc2b74`
* **Total Exported Functions:** 32

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 11 | `NhReleaseBuffer` | `0x7980` | 158 | UnwindData |  |
| 3 | `NhAcquireVariableLengthBuffer` | `0x1E070` | 375 | UnwindData |  |
| 12 | `NhWriteDatagramSocket` | `0x20CA0` | 673 | UnwindData |  |
| 9 | `NhReadDatagramSocket` | `0x241B0` | 947 | UnwindData |  |
| 6 | `NhDeleteSocket` | `0x32B90` | 250 | UnwindData |  |
| 4 | `NhCreateDatagramSocket` | `0x347D0` | 76 | UnwindData |  |
| 2 | `NhAcquireFixedLengthBuffer` | `0x35740` | 88 | UnwindData |  |
| 17 | `NatCancelDynamicRedirect` | `0x377B0` | 130 | UnwindData |  |
| 19 | `NatCreateDynamicFullRedirect` | `0x38430` | 583 | UnwindData |  |
| 15 | `SvchostPushServiceGlobals` | `0x477A0` | 135 | UnwindData |  |
| 18 | `NatCancelRedirect` | `0x48410` | 334 | UnwindData |  |
| 7 | `NhInitializeBufferManagement` | `0x50050` | 157 | UnwindData |  |
| 8 | `NhInitializeTraceManagement` | `0x55060` | 110 | UnwindData |  |
| 14 | `RegisterProtocol` | `0x55E80` | 667 | UnwindData |  |
| 1 | `NhAcceptStreamSocket` | `0x56DA0` | 1,210 | UnwindData |  |
| 5 | `NhCreateStreamSocket` | `0x57540` | 878 | UnwindData |  |
| 10 | `NhReadStreamSocket` | `0x578C0` | 837 | UnwindData |  |
| 13 | `NhWriteStreamSocket` | `0x57C10` | 593 | UnwindData |  |
| 16 | `NatAcquirePortReservation` | `0x58140` | 215 | UnwindData |  |
| 24 | `NatInitializePortReservation` | `0x58540` | 403 | UnwindData |  |
| 29 | `NatReleasePortReservation` | `0x586E0` | 236 | UnwindData |  |
| 30 | `NatShutdownPortReservation` | `0x587E0` | 108 | UnwindData |  |
| 20 | `NatCreateDynamicRedirect` | `0x58860` | 101 | UnwindData |  |
| 21 | `NatCreateDynamicRedirectEx` | `0x588D0` | 108 | UnwindData |  |
| 22 | `NatCreateRedirect` | `0x58950` | 150 | UnwindData |  |
| 23 | `NatCreateRedirectEx` | `0x589F0` | 595 | UnwindData |  |
| 25 | `NatInitializeTranslator` | `0x58D60` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `NatLookupAndQueryInformationSessionMapping` | `0x58EE0` | 499 | UnwindData |  |
| 27 | `NatQueryInformationRedirect` | `0x590E0` | 692 | UnwindData |  |
| 28 | `NatQueryInformationRedirectHandle` | `0x593A0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `NatShutdownTranslator` | `0x59460` | 114,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `ServiceMain` | `0x752A0` | 251 | UnwindData |  |
