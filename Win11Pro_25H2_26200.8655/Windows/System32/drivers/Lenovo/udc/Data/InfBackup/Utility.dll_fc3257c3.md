# Binary Specification: Utility.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\drivers\Lenovo\udc\Data\InfBackup\Utility.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fc3257c30e49b64bd48d17227e5d6f2c350a55bfba91ead5515ebba230982d82`
* **Total Exported Functions:** 69

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `??0IMqttManager@mqtt_interactions@@QEAA@AEBV01@@Z` | `0x1000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0IMqttManager@mqtt_interactions@@QEAA@XZ` | `0x1000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??1IMqttManager@mqtt_interactions@@UEAA@XZ` | `0x1010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??4IMqttManager@mqtt_interactions@@QEAAAEAV01@AEBV01@@Z` | `0x1020` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0HeartBeat@utility@common@@QEAA@V?$duration@_JU?$ratio@$00$0DOI@@std@@@chrono@std@@V?$function@$$A6AXXZ@5@1V?$duration@_JU?$ratio@$00$00@std@@@45@@Z` | `0x1260` | 440 | UnwindData |  |
| 14 | `??1HeartBeat@utility@common@@QEAA@XZ` | `0x1490` | 143 | UnwindData |  |
| 51 | `?onHeartBeat@HeartBeat@utility@common@@AEAAXW4TimerState@timer@23@@Z` | `0x15A0` | 20 | UnwindData |  |
| 57 | `?processHeartBeat@HeartBeat@utility@common@@AEAAXXZ` | `0x15C0` | 317 | UnwindData |  |
| 63 | `?resetHeartbeat@HeartBeat@utility@common@@QEAAXXZ` | `0x1700` | 45 | UnwindData |  |
| 1 | `??0BackoffStrategy@Strategy@@QEAA@AEAVLoggerCallback@utility@common@@JV?$function@$$A6AXXZ@std@@@Z` | `0x3070` | 261 | UnwindData |  |
| 10 | `??0WaitStrategy@Strategy@@QEAA@JV?$function@$$A6AXXZ@std@@@Z` | `0x32B0` | 91 | UnwindData |  |
| 11 | `??1BackoffStrategy@Strategy@@UEAA@XZ` | `0x3580` | 79 | UnwindData |  |
| 13 | `??1ExponentialBackoffStrategy@Strategy@@UEAA@XZ` | `0x3580` | 79 | UnwindData |  |
| 16 | `??1NoRetryStrategy@Strategy@@UEAA@XZ` | `0x3580` | 79 | UnwindData |  |
| 19 | `??1WaitStrategy@Strategy@@UEAA@XZ` | `0x35F0` | 45 | UnwindData |  |
| 27 | `?canExecute@WaitStrategy@Strategy@@MEAA_NXZ` | `0x3CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `?cancel@BackoffStrategy@Strategy@@QEAAXXZ` | `0x3D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `?computeWaitDurationInMillis@BackoffStrategy@Strategy@@MEAA_KAEBJ@Z` | `0x3D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `?currentTryCount@WaitStrategy@Strategy@@QEBAJXZ` | `0x3D50` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `?discardAttempt@WaitStrategy@Strategy@@MEAAXXZ` | `0x3DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `?execute@WaitStrategy@Strategy@@QEAAXXZ` | `0x3DB0` | 68 | UnwindData |  |
| 41 | `?executeStrategy@BackoffStrategy@Strategy@@MEAAXXZ` | `0x3E00` | 2,472 | UnwindData |  |
| 49 | `?isStrategyExecuting@WaitStrategy@Strategy@@QEBA_NXZ` | `0x4A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `?maxTriesAllowed@WaitStrategy@Strategy@@QEBAJXZ` | `0x4A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `?onMaxAttempt@BackoffStrategy@Strategy@@MEAAXXZ` | `0x4A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `?onMaxAttempt@WaitStrategy@Strategy@@MEAAXXZ` | `0x4A60` | 53 | UnwindData |  |
| 58 | `?reset@BackoffStrategy@Strategy@@IEAA_N_N@Z` | `0x4CB0` | 305 | UnwindData |  |
| 59 | `?reset@BackoffStrategy@Strategy@@UEAAXXZ` | `0x4DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `?reset@WaitStrategy@Strategy@@UEAAXXZ` | `0x4E00` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `?setState@BackoffStrategy@Strategy@@IEAA_NW4BackoffStrategyState@12@0_N@Z` | `0x50E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `?setStateAndNotify@BackoffStrategy@Strategy@@IEAA_NW4BackoffStrategyState@12@0_N@Z` | `0x5110` | 880 | UnwindData |  |
| 69 | `?tryReset@BackoffStrategy@Strategy@@QEAAXXZ` | `0x5560` | 519 | UnwindData |  |
| 2 | `??0CustomBackoffStrategy@Strategy@@QEAA@AEAVLoggerCallback@utility@common@@AEBV?$vector@_KV?$allocator@_K@std@@@std@@V?$function@$$A6AXXZ@6@@Z` | `0x5800` | 366 | UnwindData |  |
| 12 | `??1CustomBackoffStrategy@Strategy@@UEAA@XZ` | `0x5A70` | 178 | UnwindData |  |
| 34 | `?computeWaitDurationInMillis@CustomBackoffStrategy@Strategy@@MEAA_KAEBJ@Z` | `0x60D0` | 199 | UnwindData |  |
| 53 | `?onMaxAttempt@CustomBackoffStrategy@Strategy@@MEAAXXZ` | `0x61A0` | 70 | UnwindData |  |
| 3 | `??0ExponentialBackoffStrategy@Strategy@@QEAA@AEAVLoggerCallback@utility@common@@_K1JV?$function@$$A6AXXZ@std@@@Z` | `0x61F0` | 179 | UnwindData |  |
| 35 | `?computeWaitDurationInMillis@ExponentialBackoffStrategy@Strategy@@MEAA_KAEBJ@Z` | `0x62B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `?onMaxAttempt@ExponentialBackoffStrategy@Strategy@@MEAAXXZ` | `0x62E0` | 70 | UnwindData |  |
| 7 | `??0NoRetryStrategy@Strategy@@QEAA@AEAVLoggerCallback@utility@common@@V?$function@$$A6AXXZ@std@@@Z` | `0x6330` | 153 | UnwindData |  |
| 42 | `?executeStrategy@NoRetryStrategy@Strategy@@MEAAXXZ` | `0x6470` | 70 | UnwindData |  |
| 55 | `?onMaxAttempt@NoRetryStrategy@Strategy@@MEAAXXZ` | `0x64C0` | 70 | UnwindData |  |
| 8 | `??0ReconnectStrategyProvider@Strategy@@QEAA@AEAVLoggerCallback@utility@common@@@Z` | `0x7420` | 422 | UnwindData |  |
| 17 | `??1ReconnectStrategyProvider@Strategy@@QEAA@XZ` | `0x7780` | 67 | UnwindData |  |
| 29 | `?cancel@ReconnectStrategyProvider@Strategy@@QEAAXXZ` | `0x7C70` | 403 | UnwindData |  |
| 32 | `?computeStrategy@ReconnectStrategyProvider@Strategy@@QEAAXH@Z` | `0x7E10` | 1,000 | UnwindData |  |
| 36 | `?createStrategyPool@ReconnectStrategyProvider@Strategy@@AEAAXXZ` | `0x8200` | 2,462 | UnwindData |  |
| 39 | `?execute@ReconnectStrategyProvider@Strategy@@QEAAXXZ` | `0x8BA0` | 442 | UnwindData |  |
| 44 | `?getCurrentStrategyType@ReconnectStrategyProvider@Strategy@@AEAA?AW4StrategyType@12@XZ` | `0x8D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `?getLatestStrategy@ReconnectStrategyProvider@Strategy@@AEAAAEAV?$shared_ptr@VBackoffStrategy@Strategy@@@std@@XZ` | `0x8D70` | 178 | UnwindData |  |
| 46 | `?hasRetriesExceeded@ReconnectStrategyProvider@Strategy@@QEAA_NXZ` | `0x8E30` | 471 | UnwindData |  |
| 47 | `?hasRetriesExceededStrict@ReconnectStrategyProvider@Strategy@@QEAA_NXZ` | `0x9010` | 473 | UnwindData |  |
| 48 | `?isStrategyExecuting@ReconnectStrategyProvider@Strategy@@QEAA_NXZ` | `0x91F0` | 444 | UnwindData |  |
| 60 | `?reset@ReconnectStrategyProvider@Strategy@@QEAAXW4StrategyResetType@12@@Z` | `0x93B0` | 1,585 | UnwindData |  |
| 64 | `?setCurrentStrategyType@ReconnectStrategyProvider@Strategy@@AEAAXW4StrategyType@12@@Z` | `0x99F0` | 1,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0Timer@timer@utility@common@@QEAA@V?$duration@_JU?$ratio@$00$0DOI@@std@@@chrono@std@@V?$function@$$A6AXW4TimerState@timer@utility@common@@@Z@6@@Z` | `0xA160` | 525 | UnwindData |  |
| 18 | `??1Timer@timer@utility@common@@QEAA@XZ` | `0xA860` | 239 | UnwindData |  |
| 30 | `?cancel@Timer@timer@utility@common@@QEAAXXZ` | `0xD140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `?changeState@Timer@timer@utility@common@@AEAAXW4TimerState@234@@Z` | `0xD160` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `?expire@Timer@timer@utility@common@@QEAAXXZ` | `0xD200` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `?reset@Timer@timer@utility@common@@QEAAXXZ` | `0xD480` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `?suspend@Timer@timer@utility@common@@QEAAXXZ` | `0xD550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `?timerProcess@Timer@timer@utility@common@@AEAAXXZ` | `0xD570` | 509 | UnwindData |  |
| 24 | `??_7IMqttManager@mqtt_interactions@@6B@` | `0x104E8` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `??_7WaitStrategy@Strategy@@6B@` | `0x106E8` | 56 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `??_7BackoffStrategy@Strategy@@6B@` | `0x10720` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `??_7CustomBackoffStrategy@Strategy@@6B@` | `0x10A80` | 168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `??_7ExponentialBackoffStrategy@Strategy@@6B@` | `0x10B28` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `??_7NoRetryStrategy@Strategy@@6B@` | `0x10BB8` | 0 | Indeterminate |  |
