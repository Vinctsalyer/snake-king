def on_on_overlap(sprite, otherSprite):
    mySprite.start_effect(effects.fire, 1000)
    scene.camera_shake(4, 500)
    game.over(False, effects.splatter)
    game.reset()
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap)

mySprite: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 3 3 f f f . . . . 
            . . . f f f 3 3 3 3 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 3 3 3 3 3 3 e e f . . 
            . . f e 3 f f f f f f 3 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 3 3 3 3 3 3 f 4 e . . 
            . . 4 d f 3 3 3 3 3 3 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
snake = sprites.create(img("""
        . . . . . c c c c c c c . . . . 
            . . . . c 6 7 7 7 7 7 6 c . . . 
            . . . c 7 c 6 6 6 6 c 7 6 c . . 
            . . c 6 7 6 f 6 6 f 6 7 7 c . . 
            . . c 7 7 7 7 7 7 7 7 7 7 c . . 
            . . f 7 8 1 f f 1 6 7 7 7 f . . 
            . . f 6 f 1 f f 1 f 7 7 7 f . . 
            . . . f f 2 2 2 2 f 7 7 6 f . . 
            . . c c f 2 2 2 2 7 7 6 f c . . 
            . c 7 7 7 7 7 7 7 7 c c 7 7 c . 
            c 7 1 1 1 7 7 7 7 f c 6 7 7 7 c 
            f 1 1 1 1 1 7 6 f c c 6 6 6 c c 
            f 1 1 1 1 1 1 6 6 c 6 6 6 c . . 
            f 6 1 1 1 1 1 6 6 6 6 6 6 c . . 
            . f 6 1 1 1 1 1 6 6 6 6 c . . . 
            . . f f c c c c c c c c . . . .
    """),
    SpriteKind.enemy)
snake.follow(mySprite, 20)
snake.set_position(145, 107)
FLying_snake = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . e e . 
            . . . . 7 7 7 7 7 7 . e e e e e 
            . . . . 7 f f 7 7 7 e e e e e e 
            . . . . 7 7 7 7 7 7 7 e e e e e 
            . . . . 1 1 7 7 7 7 7 e e e e e 
            . . . . 2 2 7 7 7 7 7 7 e e . . 
            . . . 2 2 7 7 7 7 7 7 7 7 . . . 
            . . . . . . . 7 7 7 7 7 7 . . . 
            . . . . . . . . 7 7 7 7 7 . . . 
            . . . . . . . . 7 7 7 7 7 . . . 
            . . . . . . . . 7 7 7 7 . . . . 
            . . . . . . . . 7 7 7 . . . . . 
            . . . . . . . . . 7 7 . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)
FLying_snake.set_position(146, 1)
FLying_snake.follow(mySprite, 60)
Pizza = sprites.create(img("""
        . . . . . . b b b b . . . . . . 
            . . . . . . b 4 4 4 b . . . . . 
            . . . . . . b b 4 4 4 b . . . . 
            . . . . . b 4 b b b 4 4 b . . . 
            . . . . b d 5 5 5 4 b 4 4 b . . 
            . . . . b 3 2 3 5 5 4 e 4 4 b . 
            . . . b d 2 2 2 5 7 5 4 e 4 4 e 
            . . . b 5 3 2 3 5 5 5 5 e e e e 
            . . b d 7 5 5 5 3 2 3 5 5 e e e 
            . . b 5 5 5 5 5 2 2 2 5 5 d e e 
            . b 3 2 3 5 7 5 3 2 3 5 d d e 4 
            . b 2 2 2 5 5 5 5 5 5 d d e 4 . 
            b d 3 2 d 5 5 5 d d d 4 4 . . . 
            b 5 5 5 5 d d 4 4 4 4 . . . . . 
            4 d d d 4 4 4 . . . . . . . . . 
            4 4 4 4 . . . . . . . . . . . .
    """),
    SpriteKind.food)
Pizza.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
mySprite.set_flag(SpriteFlag.STAY_IN_SCREEN, True)