# Markdown格式统一脚本使用指南

## 1. 脚本功能

`unify_markdown_format.py`脚本用于统一`addlaws`目录下所有Markdown文件的格式，主要功能包括：

- 添加或更新YAML前置元数据
- 统一标题层级
- 生成目录
- 规范文本排版
- 统一条款格式
- 规范列表样式
- 自动生成URL、年份、关键词等元数据

## 2. 依赖项

- Python 3.6+
- PyYAML库

## 3. 安装依赖

```bash
pip install pyyaml
```

## 4. 配置文件

### 4.1 url_mapping.yaml

用于存储法律标题与官方URL的映射关系，格式如下：

```yaml
# URL映射表
# 格式：
# 法律标题: 官方URL

中华人民共和国宪法: https://flk.npc.gov.cn/detail2.html?MmM5MDJiNDRjYjc1YjExNGZkMTdjMjcyOGZmN2E2MWE=
中华人民共和国行政处罚法: https://flk.npc.gov.cn/detail2.html?MjkwN2U3NDY0Yjc1YjExNGZkMTdjMjcyOGZmN2E2MWE=
```

### 4.2 脚本配置

脚本中的配置变量可以根据需要调整：

- `ADDLAWS_DIR`: Markdown文件所在目录，默认为`./addlaws`
- `BACKUP_DIR`: 备份目录，默认为`./addlaws_backup`
- `ENCODING`: 文件编码，默认为`utf-8`
- `URL_MAPPING_FILE`: URL映射表文件路径，默认为`./url_mapping.yaml`
- `URL_TEMPLATES`: URL模板配置，用于生成搜索URL

## 5. 使用方法

### 5.1 基本使用

直接运行脚本，处理所有Markdown文件：

```bash
python unify_markdown_format.py
```

### 5.2 处理单个文件

目前脚本仅支持批量处理所有文件，如需处理单个文件，可以临时修改`ADDLAWS_DIR`为目标文件所在目录。

## 6. YAML元数据字段说明

脚本生成的YAML元数据包含以下字段：

| 字段名 | 说明 | 来源 |
|--------|------|------|
| id | 唯一标识符 | 自动生成的UUID |
| title | 法律标题 | 文件名 |
| LinkTitle | 链接标题 | 文件名 |
| file | 文件名 | 自动获取 |
| author | 作者 | 留空 |
| date | 处理日期 | 当前日期 |
| publication_date | 发布日期 | 留空 |
| effective_date | 生效日期 | 留空 |
| status | 状态 | 默认"有效" |
| group | 分组 | 从文件路径提取 |
| categories | 分类 | 从文件路径提取 |
| tags | 标签 | 留空 |
| years | 年份 | 从文件内容中提取 |
| keywords | 关键词 | 从文件名和内容中提取 |
| urls | 官方URL | 从映射表或生成的搜索URL |

## 7. URL生成规则

1. 首先检查`url_mapping.yaml`中是否存在对应的URL
2. 如果不存在，根据文件类型生成搜索URL：
   - 行政法规：使用国家行政法规数据库模板
   - 规章/办法：使用国家规章库模板
   - 其他：使用国家法律法规数据库模板

## 8. URL映射表维护指南

### 8.1 添加新的URL映射

1. 在官方数据库中搜索目标法律法规
2. 复制官方URL
3. 在`url_mapping.yaml`中添加新的映射条目：
   ```yaml
   法律标题: 官方URL
   ```

### 8.2 更新现有的URL映射

1. 找到需要更新的映射条目
2. 修改URL为最新的官方URL
3. 保存文件

### 8.3 最佳实践

- 定期检查和更新URL映射表
- 只添加官方网站的URL
- 确保URL的准确性和有效性

## 9. 常见问题

### 9.1 脚本运行失败

- 检查Python版本是否符合要求
- 检查依赖项是否已正确安装
- 检查配置文件路径是否正确

### 9.2 YAML元数据生成错误

- 检查文件编码是否为UTF-8
- 检查文件名是否包含特殊字符

### 9.3 URL生成不正确

- 检查`url_mapping.yaml`中是否存在对应的映射
- 检查文件路径是否正确，以便正确判断法律法规类型

## 10. 注意事项

1. 脚本会自动备份所有处理过的文件到`BACKUP_DIR`目录
2. 处理前建议先备份原始文件
3. 对于重要文件，建议手动检查处理结果
4. 定期更新URL映射表，确保URL的准确性

## 11. 扩展建议

1. 根据实际需要扩展URL模板配置
2. 完善关键词提取算法，提高关键词的准确性
3. 增加对更多法律法规类型的支持
4. 添加手动干预机制，允许用户调整生成的元数据

## 12. 联系方式

如有问题或建议，请联系相关技术人员。
