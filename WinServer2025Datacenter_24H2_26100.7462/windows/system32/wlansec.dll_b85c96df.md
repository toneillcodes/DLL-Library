# Binary Specification: wlansec.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wlansec.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b85c96dfb06026c4b898aed380ad35256b40c3db0febb7a36eb04deaed4df04a`
* **Total Exported Functions:** 34

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 32 | `MSMSecStopPostAssociateSecurity` | `0x10760` | 1,725 | UnwindData |  |
| 23 | `MSMSecRecvIndication` | `0x10E30` | 1,916 | UnwindData |  |
| 19 | `MSMSecProcessSessionChange` | `0x11BB0` | 490 | UnwindData |  |
| 15 | `MSMSecPerformCapabilityMatch` | `0x11FB0` | 2,610 | UnwindData |  |
| 33 | `MSMSecStopSecurity` | `0x139C0` | 758 | UnwindData |  |
| 16 | `MSMSecPerformPostAssociateSecurity` | `0x14670` | 2,199 | UnwindData |  |
| 27 | `MSMSecSendPktCompletion` | `0x16720` | 447 | UnwindData |  |
| 24 | `MSMSecRecvPacket` | `0x18240` | 1,779 | UnwindData |  |
| 4 | `MSMSecDeinitializeAdapter` | `0x22010` | 396 | UnwindData |  |
| 13 | `MSMSecInitializeAdapter` | `0x23980` | 573 | UnwindData |  |
| 26 | `MSMSecRemoveAPPeerKey` | `0x28290` | 819 | UnwindData |  |
| 5 | `MSMSecDisableIpAddressAllocation` | `0x291F0` | 751 | UnwindData |  |
| 34 | `MSMSecUIResponse` | `0x323D0` | 1,221 | UnwindData |  |
| 30 | `MSMSecSetRuntimeState` | `0x33070` | 1,296 | UnwindData |  |
| 17 | `MSMSecPerformPreAssociateSecurity` | `0x3A970` | 94 | UnwindData |  |
| 18 | `MSMSecPerformPreAssociateSecurityEx` | `0x3A9E0` | 3,003 | UnwindData |  |
| 8 | `MSMSecFreeMemory` | `0x3BA60` | 350 | UnwindData |  |
| 6 | `MSMSecEnableIpAddressAllocation` | `0x3D800` | 773 | UnwindData |  |
| 1 | `MSMSecConnectionHealthCheck` | `0x51B10` | 935 | UnwindData |  |
| 2 | `MSMSecCreateDiscoveryProfiles` | `0x51EC0` | 1,541 | UnwindData |  |
| 3 | `MSMSecDeinitialize` | `0x524D0` | 292 | UnwindData |  |
| 7 | `MSMSecFreeIntfState` | `0x52600` | 279 | UnwindData |  |
| 9 | `MSMSecFreePeerState` | `0x52720` | 277 | UnwindData |  |
| 10 | `MSMSecFreeProfile` | `0x52840` | 315 | UnwindData |  |
| 11 | `MSMSecGetPeerIpAddress` | `0x52990` | 782 | UnwindData |  |
| 12 | `MSMSecInitialize` | `0x52CB0` | 288 | UnwindData |  |
| 14 | `MSMSecIsUIRequestPending` | `0x52DE0` | 734 | UnwindData |  |
| 20 | `MSMSecQueryAPPeerPSKIndex` | `0x530D0` | 777 | UnwindData |  |
| 21 | `MSMSecQueryIntfState` | `0x533E0` | 558 | UnwindData |  |
| 22 | `MSMSecQueryPeerState` | `0x53620` | 1,179 | UnwindData |  |
| 25 | `MSMSecRedoSecurity` | `0x53AD0` | 1,938 | UnwindData |  |
| 28 | `MSMSecSetAPPeerKey` | `0x54270` | 1,732 | UnwindData |  |
| 29 | `MSMSecSetAPSecondaryPSK` | `0x54940` | 918 | UnwindData |  |
| 31 | `MSMSecSetWcnOneXEnable` | `0x54CE0` | 970 | UnwindData |  |
