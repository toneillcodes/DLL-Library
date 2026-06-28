# Binary Specification: clfsw32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\clfsw32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d04a74404298f0aa2e4fc9695d4a840479d35f60837d79ec0dd6e221674ca5d1`
* **Total Exported Functions:** 63

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `AddLogContainer` | `0x3EE0` | 66 | UnwindData |  |
| 3 | `AddLogContainerSet` | `0x3F30` | 1,130 | UnwindData |  |
| 4 | `AdvanceLogBase` | `0x43A0` | 116 | UnwindData |  |
| 5 | `AlignReservedLog` | `0x4420` | 209 | UnwindData |  |
| 6 | `AllocReservedLog` | `0x4500` | 98 | UnwindData |  |
| 9 | `CloseAndResetLogFile` | `0x4570` | 315 | UnwindData |  |
| 10 | `CreateLogContainerScanContext` | `0x46C0` | 646 | UnwindData |  |
| 11 | `CreateLogFile` | `0x4950` | 2,102 | UnwindData |  |
| 12 | `CreateLogMarshallingArea` | `0x5190` | 350 | UnwindData |  |
| 13 | `DeleteLogByHandle` | `0x5300` | 95 | UnwindData |  |
| 14 | `DeleteLogFile` | `0x5370` | 208 | UnwindData |  |
| 15 | `DeleteLogMarshallingArea` | `0x5450` | 91 | UnwindData |  |
| 16 | `DeregisterManageableLogClient` | `0x54C0` | 93 | UnwindData |  |
| 17 | `DumpLogRecords` | `0x5890` | 1,932 | UnwindData |  |
| 18 | `FlushLogBuffers` | `0x6030` | 134 | UnwindData |  |
| 19 | `FlushLogToLsn` | `0x60C0` | 139 | UnwindData |  |
| 20 | `FreeReservedLog` | `0x6160` | 89 | UnwindData |  |
| 21 | `GetLogContainerName` | `0x61C0` | 354 | UnwindData |  |
| 22 | `GetLogFileInformation` | `0x6330` | 123 | UnwindData |  |
| 23 | `GetLogIoStatistics` | `0x63C0` | 350 | UnwindData |  |
| 24 | `GetLogReservationInfo` | `0x6530` | 99 | UnwindData |  |
| 25 | `GetNextLogArchiveExtent` | `0x65A0` | 115 | UnwindData |  |
| 26 | `HandleLogFull` | `0x6620` | 141 | UnwindData |  |
| 27 | `InstallLogPolicy` | `0x66C0` | 108 | UnwindData |  |
| 28 | `LogTailAdvanceFailure` | `0x6740` | 149 | UnwindData |  |
| 32 | `LsnEqual` | `0x67E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `LsnGreater` | `0x6800` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `LsnLess` | `0x6830` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `PrepareLogArchive` | `0x6860` | 997 | UnwindData |  |
| 40 | `QueryLogPolicy` | `0x6C50` | 285 | UnwindData |  |
| 41 | `ReadLogArchiveMetadata` | `0x6D80` | 152 | UnwindData |  |
| 42 | `ReadLogNotification` | `0x6E20` | 107 | UnwindData |  |
| 43 | `ReadLogRecord` | `0x6EA0` | 342 | UnwindData |  |
| 44 | `ReadLogRestartArea` | `0x7000` | 155 | UnwindData |  |
| 45 | `ReadNextLogRecord` | `0x70B0` | 521 | UnwindData |  |
| 46 | `ReadPreviousLogRestartArea` | `0x72C0` | 246 | UnwindData |  |
| 47 | `RegisterForLogWriteNotification` | `0x73C0` | 159 | UnwindData |  |
| 48 | `RegisterManageableLogClient` | `0x7470` | 153 | UnwindData |  |
| 49 | `RemoveLogContainer` | `0x7510` | 62 | UnwindData |  |
| 50 | `RemoveLogContainerSet` | `0x7560` | 1,105 | UnwindData |  |
| 51 | `RemoveLogPolicy` | `0x79C0` | 100 | UnwindData |  |
| 52 | `ReserveAndAppendLog` | `0x7A30` | 379 | UnwindData |  |
| 53 | `ReserveAndAppendLogAligned` | `0x7BC0` | 393 | UnwindData |  |
| 54 | `ScanLogContainers` | `0x7D50` | 514 | UnwindData |  |
| 55 | `SetEndOfLog` | `0x7F60` | 272 | UnwindData |  |
| 56 | `SetLogArchiveMode` | `0x8080` | 325 | UnwindData |  |
| 57 | `SetLogArchiveTail` | `0x81D0` | 104 | UnwindData |  |
| 58 | `SetLogFileSizeWithPolicy` | `0x8240` | 124 | UnwindData |  |
| 59 | `TerminateLogArchive` | `0x82D0` | 93 | UnwindData |  |
| 60 | `TerminateReadLog` | `0x8340` | 121 | UnwindData |  |
| 61 | `TruncateLog` | `0x83C0` | 101 | UnwindData |  |
| 62 | `ValidateLog` | `0x8430` | 309 | UnwindData |  |
| 63 | `WriteLogRestartArea` | `0x86D0` | 279 | UnwindData |  |
| 1 | `LsnDecrement` | `0xBFC0` | 14,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `LsnBlockOffset` | `0xF710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `LsnContainer` | `0xF730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `LsnCreate` | `0xF750` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `LsnIncrement` | `0xF790` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `LsnInvalid` | `0xF7E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `LsnNull` | `0xF800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `LsnRecordSequence` | `0xF820` | 22,784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `CLFS_LSN_INVALID` | `0x15120` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `CLFS_LSN_NULL` | `0x15148` | 0 | Indeterminate |  |
