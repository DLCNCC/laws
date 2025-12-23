# 行政执法和行政执法合规文件夹多级目录创建方案

## 一、实施目标

为以下两个文件夹实现左侧多级目录：
- `c:\Users\zp053\Desktop\lawnav.github.io\content\行政执法`
- `c:\Users\zp053\Desktop\lawnav.github.io\content\行政执法合规`

## 二、实施内容

### 1. 修改顶级 _index.md 文件

#### 1.1 行政执法/_index.md
```yaml
---
title: 行政执法
linkTitle: 行政执法
type: "docs"
cascade: { type: "docs" }
menu: {main: {weight: 3}}
bookCollapseSection: true
---
```

#### 1.2 行政执法合规/_index.md
```yaml
---
title: 行政执法合规
linkTitle: 行政执法合规
type: "docs"
cascade: { type: "docs" }
menu: {main: {weight: 4}}
bookCollapseSection: true
---
```

### 2. 为所有子目录创建 _index.md 文件

#### 2.1 目录遍历规则
- 遍历文件夹下所有子目录
- 为每个子目录创建 _index.md 文件
- 自动识别目录层级和父目录关系
- 生成合适的 title、linkTitle 和 menu 配置

#### 2.2 子目录 _index.md 文件模板

##### 二级子目录示例（如行政执法/交通运输）
```yaml
---
title: 交通运输
linkTitle: 交通运输
type: "docs"
menu: {main: {parent: "行政执法", weight: 1}}
bookCollapseSection: true
---
```

##### 三级子目录示例（如行政执法/交通运输/01.执法程序规定）
```yaml
---
title: 01.执法程序规定
linkTitle: 01.执法程序规定
type: "docs"
menu: {main: {parent: "交通运输", weight: 1}}
---
```

##### 四级子目录示例（如行政执法/交通运输/02.道路运输/旅客运输管理）
```yaml
---
title: 旅客运输管理
linkTitle: 旅客运输管理
type: "docs"
menu: {main: {parent: "道路运输", weight: 1}}
---
```

### 3. 权重分配规则
- 按照目录名称的数字前缀自动分配权重
- 无前缀目录按照字母顺序分配权重
- 确保目录在导航中显示顺序合理

## 三、实施步骤

### 1. 准备工作
- 备份现有 _index.md 文件
- 确认 Hugo 主题支持 Docsy 目录功能

### 2. 修改顶级 _index.md 文件
- 使用上述内容修改 `行政执法/_index.md`
- 使用上述内容修改 `行政执法合规/_index.md`

### 3. 遍历子目录创建 _index.md 文件

#### 3.1 行政执法文件夹子目录
- 交通运输
- 住建
- 公共法律
- 农业农村
- 以及它们的所有子目录

#### 3.2 行政执法合规文件夹子目录
- 01依法治国依法行政相关文件
- 02行政执法合规的相关制度
- 03行政执法合规法律法规
- 04行政执法程序
- 05行政处罚自由裁量权规定
- 06行政执法三项制度
- 08行政执法案卷
- 09行政执法监督
- 10行政执法责任追究相关规定
- 12行政复议与诉讼
- 以及它们的所有子目录

### 4. 验证和测试
- 运行 `hugo server` 启动本地服务器
- 检查左侧导航是否正确显示多级目录
- 测试折叠/展开功能
- 验证目录跳转是否正常

## 四、预期效果

1. **左侧导航**：显示完整的多级目录结构
2. **折叠功能**：支持目录的折叠和展开
3. **层级清晰**：通过缩进直观显示目录层级关系
4. **自动高亮**：当前浏览的页面在导航中自动高亮
5. **响应式设计**：在不同设备上都有良好的显示效果

## 五、后续维护

- 新增子目录时，需手动创建对应的 _index.md 文件
- 根据内容重要性调整 menu.weight 参数
- 定期检查目录结构，确保导航正常显示

## 六、实施工具

- 使用 Python 脚本自动生成子目录 _index.md 文件
- 手动修改顶级 _index.md 文件
- 使用 Hugo 本地服务器验证效果

通过以上方案，将为行政执法和行政执法合规文件夹实现完整的左侧多级目录功能，提升用户的浏览体验和内容查找效率。