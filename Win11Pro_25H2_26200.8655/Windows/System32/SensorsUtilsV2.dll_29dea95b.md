# Binary Specification: SensorsUtilsV2.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\SensorsUtilsV2.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `29dea95bf366b16fd71a3c623ed7a0399899f6176820483043cbf6ff9975cb3c`
* **Total Exported Functions:** 71

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 35 | `GetSetting` | `0xA3C0` | 4,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `AddMillisecondsToFileTime` | `0xB510` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CollectionsListAllocateBufferAndSerialize` | `0xB550` | 399 | UnwindData |  |
| 3 | `CollectionsListCopyAndMarshall` | `0xB6F0` | 419 | UnwindData |  |
| 4 | `CollectionsListDeserializeFromBuffer` | `0xB8A0` | 1,324 | UnwindData |  |
| 5 | `CollectionsListGetFillableCount` | `0xBDE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `CollectionsListGetMarshalledSize` | `0xBE10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `CollectionsListGetMarshalledSizeWithoutSerialization` | `0xBE30` | 131 | UnwindData |  |
| 8 | `CollectionsListGetSerializedSize` | `0xBEC0` | 500 | UnwindData |  |
| 9 | `CollectionsListMarshall` | `0xC0C0` | 390 | UnwindData |  |
| 10 | `CollectionsListSerializeToBuffer` | `0xC250` | 881 | UnwindData |  |
| 11 | `CollectionsListSortSubscribedActivitiesByConfidence` | `0xC5D0` | 1,175 | UnwindData |  |
| 12 | `CollectionsListUpdateMarshalledPointer` | `0xCA70` | 268 | UnwindData |  |
| 13 | `ConvertAccelerometerDataToCollection` | `0xCB90` | 206 | UnwindData |  |
| 14 | `ConvertCollectionToAccelerometerData` | `0xCC70` | 200 | UnwindData |  |
| 15 | `ConvertCollectionToGyroscopeData` | `0xCEA0` | 98 | UnwindData |  |
| 16 | `ConvertCollectionToLightSensorData` | `0xCF10` | 27 | UnwindData |  |
| 17 | `ConvertCollectionToLightSensorDataWithColor` | `0xCF40` | 645 | UnwindData |  |
| 18 | `ConvertCollectionToMagnetometerData` | `0xD1D0` | 168 | UnwindData |  |
| 19 | `ConvertCollectionToOrientationData` | `0xD280` | 827 | UnwindData |  |
| 20 | `ConvertCollectionToProximitySensorData` | `0xD5D0` | 201 | UnwindData |  |
| 21 | `ConvertFloat3DDataToCollection` | `0xD6A0` | 207 | UnwindData |  |
| 22 | `ConvertGyroscopeDataToCollection` | `0xD780` | 99 | UnwindData |  |
| 23 | `ConvertLightSensorDataToCollection` | `0xD7F0` | 115 | UnwindData |  |
| 24 | `ConvertLightSensorDataWithColorToCollection` | `0xD870` | 357 | UnwindData |  |
| 25 | `ConvertMagnetometerDataToCollection` | `0xD9E0` | 200 | UnwindData |  |
| 26 | `ConvertOrientationDataToCollection` | `0xDAB0` | 708 | UnwindData |  |
| 27 | `ConvertProximitySensorDataToCollection` | `0xDD80` | 170 | UnwindData |  |
| 28 | `ConvertSimpleOrientationDataToCollection` | `0xDE30` | 115 | UnwindData |  |
| 29 | `EvaluateActivityThresholds` | `0xDEB0` | 1,157 | UnwindData |  |
| 30 | `GetBiosInformation` | `0xE340` | 204 | UnwindData |  |
| 31 | `GetDeviceClassStr` | `0xE420` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `GetFileTimeDifference` | `0xE470` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `GetFileTimeFromTimeStamp` | `0xE4C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `GetTimeStampFromFileTime` | `0xE4C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `GetPerformanceTime` | `0xE4E0` | 243 | UnwindData |  |
| 36 | `GetSystemTableInfo` | `0xE5E0` | 285 | UnwindData |  |
| 38 | `InitPropVariantFromCLSIDArray` | `0xE710` | 141 | UnwindData |  |
| 39 | `InitPropVariantFromFloat` | `0xE7B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `InitPropVariantFromFloatVector` | `0xE7D0` | 158 | UnwindData |  |
| 41 | `IsCollectionListSame` | `0xEA20` | 317 | UnwindData |  |
| 42 | `IsGUIDPresentInList` | `0xEB70` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `IsKeyPresentInCollectionList` | `0xEBB0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `IsKeyPresentInPropertyList` | `0xEC10` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `IsSensorSubscribed` | `0xECB0` | 125 | UnwindData |  |
| 46 | `IsTestSigningOn` | `0xED40` | 115 | UnwindData |  |
| 47 | `MapActivityConfidenceToState` | `0xEE50` | 353 | UnwindData |  |
| 48 | `PropKeyFindKeyGetBool` | `0xEFC0` | 137 | UnwindData |  |
| 49 | `PropKeyFindKeyGetDouble` | `0xF050` | 137 | UnwindData |  |
| 50 | `PropKeyFindKeyGetFileTime` | `0xF0E0` | 124 | UnwindData |  |
| 51 | `PropKeyFindKeyGetFloat` | `0xF170` | 113 | UnwindData |  |
| 52 | `PropKeyFindKeyGetGuid` | `0xF1F0` | 137 | UnwindData |  |
| 53 | `PropKeyFindKeyGetInt32` | `0xF280` | 137 | UnwindData |  |
| 54 | `PropKeyFindKeyGetInt64` | `0xF310` | 137 | UnwindData |  |
| 55 | `PropKeyFindKeyGetNthInt64` | `0xF3A0` | 177 | UnwindData |  |
| 56 | `PropKeyFindKeyGetNthUlong` | `0xF460` | 177 | UnwindData |  |
| 57 | `PropKeyFindKeyGetNthUshort` | `0xF520` | 177 | UnwindData |  |
| 58 | `PropKeyFindKeyGetPropVariant` | `0xF5E0` | 195 | UnwindData |  |
| 59 | `PropKeyFindKeyGetUlong` | `0xF6B0` | 137 | UnwindData |  |
| 60 | `PropKeyFindKeyGetUshort` | `0xF740` | 137 | UnwindData |  |
| 61 | `PropKeyFindKeySetPropVariant` | `0xF7D0` | 195 | UnwindData |  |
| 62 | `PropVariantGetInformation` | `0xF8A0` | 327 | UnwindData |  |
| 63 | `PropVariantToFloatVector` | `0xF9F0` | 84 | UnwindData |  |
| 64 | `PropertiesListCopy` | `0xFA50` | 187 | UnwindData |  |
| 65 | `PropertiesListGetFillableCount` | `0xFB20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `SensorCollectionGetAt` | `0xFB50` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `SensorsQueryDeviceCompatFlags` | `0xFBD0` | 186 | UnwindData |  |
| 68 | `SensorsQueryDeviceCompatFlagsUsingSmbiosInformation` | `0xFC90` | 443 | UnwindData |  |
| 69 | `SensorsQueryDeviceCompatFlagsUsingSystemInformation` | `0xFE60` | 418 | UnwindData |  |
| 70 | `SerializationBufferAllocate` | `0x10010` | 99 | UnwindData |  |
| 71 | `SerializationBufferFree` | `0x10080` | 27 | UnwindData |  |
