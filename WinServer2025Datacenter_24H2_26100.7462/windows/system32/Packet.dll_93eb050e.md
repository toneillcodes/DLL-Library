# Binary Specification: Packet.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Packet.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `93eb050ef62640906b252b49b4cce7229bcf9d2b1149583073c386b5986a74c2`
* **Total Exported Functions:** 40

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 17 | `PacketGetVersion` | `0x3420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `PacketGetDriverVersion` | `0x3430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `PacketGetDriverName` | `0x3440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `PacketStopDriver` | `0x3450` | 198 | UnwindData |  |
| 22 | `PacketOpenAdapter` | `0x3520` | 1,191 | UnwindData |  |
| 3 | `PacketCloseAdapter` | `0x39D0` | 128 | UnwindData |  |
| 2 | `PacketAllocatePacket` | `0x3A50` | 71 | UnwindData |  |
| 4 | `PacketFreePacket` | `0x3AA0` | 35 | UnwindData |  |
| 18 | `PacketInitPacket` | `0x3AD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `PacketReceivePacket` | `0x3B00` | 158 | UnwindData |  |
| 25 | `PacketSendPacket` | `0x3CD0` | 154 | UnwindData |  |
| 26 | `PacketSendPackets` | `0x3D70` | 112 | UnwindData |  |
| 33 | `PacketSetMinToCopy` | `0x4010` | 151 | UnwindData |  |
| 34 | `PacketSetMode` | `0x40B0` | 150 | UnwindData |  |
| 19 | `PacketIsDumpEnded` | `0x4150` | 22 | UnwindData |  |
| 29 | `PacketSetDumpLimits` | `0x4150` | 22 | UnwindData |  |
| 30 | `PacketSetDumpName` | `0x4150` | 22 | UnwindData |  |
| 13 | `PacketGetReadEvent` | `0x4170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `PacketSetNumWrites` | `0x4180` | 120 | UnwindData |  |
| 37 | `PacketSetReadTimeout` | `0x4200` | 63 | UnwindData |  |
| 28 | `PacketSetBuff` | `0x4240` | 145 | UnwindData |  |
| 27 | `PacketSetBpf` | `0x42E0` | 155 | UnwindData |  |
| 32 | `PacketSetLoopbackBehavior` | `0x4380` | 120 | UnwindData |  |
| 39 | `PacketSetTimestampMode` | `0x4400` | 120 | UnwindData |  |
| 16 | `PacketGetTimestampModes` | `0x4480` | 166 | UnwindData |  |
| 38 | `PacketSetSnapLen` | `0x4530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `PacketGetStats` | `0x4540` | 237 | UnwindData |  |
| 15 | `PacketGetStatsEx` | `0x4630` | 262 | UnwindData |  |
| 24 | `PacketRequest` | `0x4740` | 69 | UnwindData |  |
| 31 | `PacketSetHwFilter` | `0x4790` | 260 | UnwindData |  |
| 5 | `PacketGetAdapterNames` | `0x48A0` | 41 | UnwindData |  |
| 11 | `PacketGetNetInfoEx` | `0x4C40` | 86 | UnwindData |  |
| 12 | `PacketGetNetType` | `0x5150` | 293 | UnwindData |  |
| 20 | `PacketIsLoopbackAdapter` | `0x5310` | 95 | UnwindData |  |
| 21 | `PacketIsMonitorModeSupported` | `0x5370` | 85 | UnwindData |  |
| 35 | `PacketSetMonitorMode` | `0x54F0` | 171 | UnwindData |  |
| 10 | `PacketGetMonitorMode` | `0x5700` | 85 | UnwindData |  |
| 6 | `PacketGetAirPcapHandle` | `0x58E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `PacketGetInfo` | `0x5900` | 201 | UnwindData |  |
| 1 | `PacketLibraryVersion` | `0x2E19C` | 0 | Indeterminate |  |
