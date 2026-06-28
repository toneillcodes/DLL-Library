# Binary Specification: WFDSConMgr.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WFDSConMgr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cd331e915a6807b386e38c47be6a042c92428097444ea8f772f2a53770b2fde4`
* **Total Exported Functions:** 21

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `WFDSConMgrConfigureFirewallForInfraCast` | `0xDD80` | 4,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `WFDSConMgrCloseSessionContext` | `0xF0D0` | 177 | UnwindData |  |
| 3 | `WFDSConMgrConnect` | `0xF190` | 48 | UnwindData |  |
| 4 | `WFDSConMgrConnectTransport` | `0xF1D0` | 48 | UnwindData |  |
| 5 | `WFDSConMgrDisconnect` | `0xF210` | 39 | UnwindData |  |
| 6 | `WFDSConMgrDisconnectTransport` | `0xF240` | 33 | UnwindData |  |
| 7 | `WFDSConMgrFreeMemory` | `0xF270` | 147 | UnwindData |  |
| 8 | `WFDSConMgrGetOpenSessionList` | `0xF310` | 25 | UnwindData |  |
| 9 | `WFDSConMgrGetTransportBitmaskFromMultistring` | `0xF330` | 410 | UnwindData |  |
| 10 | `WFDSConMgrIntCompleteInfracastConnection` | `0xF4D0` | 39 | UnwindData |  |
| 11 | `WFDSConMgrIntGetInfracastBackchannelParams` | `0xF500` | 34 | UnwindData |  |
| 12 | `WFDSConMgrIntGetRtspConnectionParams` | `0xF530` | 34 | UnwindData |  |
| 14 | `WFDSConMgrOpenSessionContext` | `0xF560` | 59 | UnwindData |  |
| 15 | `WFDSConMgrOpenSessionContextForMacAddress` | `0xF5B0` | 59 | UnwindData |  |
| 16 | `WFDSConMgrOpenSessionContextForNotification` | `0xF600` | 60 | UnwindData |  |
| 17 | `WFDSConMgrQueryCorrelationId` | `0xF650` | 34 | UnwindData |  |
| 18 | `WFDSConMgrQueryStatus` | `0xF680` | 46 | UnwindData |  |
| 19 | `WFDSConMgrReadCeremonyData` | `0xF6C0` | 46 | UnwindData |  |
| 20 | `WFDSConMgrSetAllowRemoteInput` | `0xF700` | 34 | UnwindData |  |
| 21 | `WFDSConMgrWriteCeremonyData` | `0xF730` | 46 | UnwindData |  |
| 13 | `WFDSConMgrNewDiscoveredEntryOverwritesOld` | `0x109D0` | 770 | UnwindData |  |
