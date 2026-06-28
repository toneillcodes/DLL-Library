# Binary Specification: WFDSConMgr.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WFDSConMgr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d724ed3dff0a366d97b4bfa29ab240f14d411c252414122aaad7e29b1a47ce8b`
* **Total Exported Functions:** 21

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `WFDSConMgrConfigureFirewallForInfraCast` | `0x6520` | 2,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `WFDSConMgrCloseSessionContext` | `0x6DF0` | 39 | UnwindData |  |
| 3 | `WFDSConMgrConnect` | `0x6E20` | 48 | UnwindData |  |
| 4 | `WFDSConMgrConnectTransport` | `0x6E60` | 48 | UnwindData |  |
| 5 | `WFDSConMgrDisconnect` | `0x6EA0` | 39 | UnwindData |  |
| 6 | `WFDSConMgrDisconnectTransport` | `0x6ED0` | 33 | UnwindData |  |
| 7 | `WFDSConMgrFreeMemory` | `0x6F00` | 147 | UnwindData |  |
| 8 | `WFDSConMgrGetOpenSessionList` | `0x6FA0` | 25 | UnwindData |  |
| 9 | `WFDSConMgrGetTransportBitmaskFromMultistring` | `0x6FC0` | 410 | UnwindData |  |
| 10 | `WFDSConMgrIntCompleteInfracastConnection` | `0x7160` | 39 | UnwindData |  |
| 11 | `WFDSConMgrIntGetInfracastBackchannelParams` | `0x7190` | 34 | UnwindData |  |
| 12 | `WFDSConMgrIntGetRtspConnectionParams` | `0x71C0` | 34 | UnwindData |  |
| 14 | `WFDSConMgrOpenSessionContext` | `0x71F0` | 59 | UnwindData |  |
| 15 | `WFDSConMgrOpenSessionContextForMacAddress` | `0x7240` | 59 | UnwindData |  |
| 16 | `WFDSConMgrOpenSessionContextForNotification` | `0x7290` | 60 | UnwindData |  |
| 17 | `WFDSConMgrQueryCorrelationId` | `0x72E0` | 34 | UnwindData |  |
| 18 | `WFDSConMgrQueryStatus` | `0x7310` | 46 | UnwindData |  |
| 19 | `WFDSConMgrReadCeremonyData` | `0x7350` | 46 | UnwindData |  |
| 20 | `WFDSConMgrSetAllowRemoteInput` | `0x7390` | 34 | UnwindData |  |
| 21 | `WFDSConMgrWriteCeremonyData` | `0x73C0` | 46 | UnwindData |  |
| 13 | `WFDSConMgrNewDiscoveredEntryOverwritesOld` | `0xD9A0` | 770 | UnwindData |  |
